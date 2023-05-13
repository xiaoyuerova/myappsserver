from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import SpecialSubmit


class SpecialSubmitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpecialSubmit
        fields = ['id', 'WjId', 'Number', 'Data', 'Time', 'SubmitIp', 'UseTime', 'Agent', 'Answer']
