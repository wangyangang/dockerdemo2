from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from django.http import JsonResponse

from . import models


class ClassSerializer(ModelSerializer):
    class Meta:
        model = models.Classes
        fields = '__all__'


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'


class IndexView(ModelViewSet):
    queryset = models.Classes.objects.all()
    serializer_class = ClassSerializer


class TeacherListView(ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer

