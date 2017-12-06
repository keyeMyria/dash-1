from rest_framework import serializers

from project.models import Member, Group, Category, Project
from .user import UserSerializer
from .tag import TagSerializer


class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        fields = ('id', 'project', 'user', 'role')


class GroupSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True)

    class Meta:
        model = Group
        fields = ('id', 'project', 'members')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    category = CategorySerializer()
    deleted_by = UserSerializer()
    completed_by = UserSerializer()
    tags = serializers.SerializerMethodField()

    def get_tags(self, obj):
        return [TagSerializer(t).data for t in obj.tags.all()]

    class Meta:
        model = Project
        fields = '__all__'
