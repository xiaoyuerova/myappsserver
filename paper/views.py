from .models import Paper
from .serializers import PaperSerializer
import pandas as pd
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .manage_temp.admin import *


class PaperList(APIView):
    """
    列出所有的snippets或者创建一个新的snippet。
    """

    def get(self, request):

        papers = Paper.objects.filter(Select1__exact=False, Locked__exact=False,
                                      Complete__exact=False)[:5]
        # 操作中上锁
        for paper in papers:
            paper.Locked = True
            paper.save()
        # print('paper list: ', len(papers))
        serializer = PaperSerializer(papers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaperDetail(APIView):
    """
    检索，更新或删除一个snippet示例。
    """

    def get_object(self, uid):
        try:
            return Paper.objects.get(Uid=uid)
        except Paper.DoesNotExist:
            raise Http404

    def get(self, request, uid):
        paper = self.get_object(uid)
        serializer = PaperSerializer(paper)
        return Response(serializer.data)

    def put(self, request, uid):
        paper = self.get_object(uid)
        serializer = PaperSerializer(paper, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uid):
        paper = self.get_object(uid)
        paper.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaperManege(APIView):
    operates = {
        'init': init_data,
        'delete': delete_data,
        'download': download_data,
        'refresh': refresh_data
    }

    def put(self, request, opt):
        if opt in self.operates.keys():
            self.operates.get(opt)()
            return Response(status=status.HTTP_200_OK)
        Response("opt error")


