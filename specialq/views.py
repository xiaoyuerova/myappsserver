import json

from django.shortcuts import render
from .models import SpecialSubmit
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from specialq.serializers import SpecialSubmitSerializer

from rest_framework.decorators import api_view
from django.db.models import Max


# Create your views here.


class SpecialSubmitList(APIView):
    """
    列出所有的snippets
    """

    def get(self, request, wjid=None):

        if wjid is None:
            submit = SpecialSubmit.objects.all()
            serializer = SpecialSubmitSerializer(submit, many=True)
            return Response(serializer.data)
        else:
            try:
                submit = SpecialSubmit.objects.filter(WjId__exact=wjid)
                serializer = SpecialSubmitSerializer(submit, many=True)
                return Response(serializer.data)
            except SpecialSubmit.DoesNotExist:
                raise Http404

    def post(self, request):
        serializer = SpecialSubmitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecialSubmitDetail(APIView):
    """
    检索，更新或删除一个snippet示例。
    """

    def get_object(self, wjid, agent):
        try:
            return SpecialSubmit.objects.get(WjId=wjid, Agent=agent)
        except SpecialSubmit.DoesNotExist:
            raise Http404

    def get(self, request, wjid, agent):
        submit = self.get_object(wjid, agent)
        serializer = SpecialSubmitSerializer(submit)
        return Response(serializer.data)

    def put(self, request, wjid, agent):
        submit = self.get_object(wjid, agent)
        serializer = SpecialSubmitSerializer(submit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, wjid, agent):
        submit = self.get_object(wjid, agent)
        submit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def submit(request):
    """
    创建一个新的snippet。
    需要的参数包括['WjId', 'SubmitIp', 'UseTime', 'Agent', 'Answer']
    全部参数['WjId', 'Number', 'Data', 'Time', 'SubmitIp', 'UseTime', 'Agent', 'Answer']
    """
    if request.method == 'POST':
        data = request.data
        max_num = SpecialSubmit.objects.filter(WjId=data['WjId']).aggregate(Max('Number'))['Number__max']
        data._mutable = True
        data['Number'] = max_num + 1 if max_num is not None else 1
        data['SubmitIp'] = request.headers['Host']
        data['Agent'] = request.headers['User-Agent']

        serializer = SpecialSubmitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def authentic(request):
    """
    验证是否已经提交过问卷
    """
    if request.method == 'POST':
        data = request.data
        wjid = data['WjId']
        agent = request.headers['User-Agent']

        try:
            special = SpecialSubmit.objects.get(WjId__exact=wjid, Agent__exact=agent)
            serializer = SpecialSubmitSerializer(special)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SpecialSubmit.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
