from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from django.http import JsonResponse

from . import models


class PageSerializer(ModelSerializer):
    class Meta:
        model = models.Classes
        fields = '__all__'


class IndexView(ModelViewSet):
    queryset = models.Classes.objects.all()
    serializer_class = PageSerializer
    # def get(self, request):
    #     #return self.list(request)
    #     return JsonResponse("{}")
