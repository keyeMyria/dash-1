from urllib.parse import unquote_plus

from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.models import Folder, File
from .user import UserSerializer
from .tag import TagSerializer

User = get_user_model()


class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = ('id', 'name', 'parent', 'project')


class FileSerializer(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = File
        fields = '__all__'
