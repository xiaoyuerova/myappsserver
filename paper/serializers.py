from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Paper


class PaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paper
        fields = ['Uid', 'Title', 'Author', 'Abstract', 'Title_CN', 'Abstract_CN', 'Link', 'Meeting', 'Complete',
                  'Locked', 'Select1', 'Select2']
