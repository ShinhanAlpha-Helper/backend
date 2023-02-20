from django.shortcuts import render
from rest_framework import generics, mixins
from .models import DomesticNews, OverseasNews

from .serializers import (
    DomesticNewsSerializer,
    OverseasNewsSerializer,
)

from rest_framework.response import Response
from rest_framework import status

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Create your views here.

class DomesticNewsView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = DomesticNewsSerializer

    def get_queryset(self):
        return DomesticNews.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    

class OverseasNewsView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = OverseasNewsSerializer

    def get_queryset(self):
        return OverseasNews.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

