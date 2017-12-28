from django_filters import rest_framework as filters
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response

from core.models import Apply
from api.serializers import ApplySerializer


class ApplyViewSet(viewsets.ModelViewSet):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer
