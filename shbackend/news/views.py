from django.shortcuts import render
from rest_framework import generics, mixins
from .models import DomesticNews, OverseasNews

from .serializers import (
    DomesticNewsSerializer,
    OverseasNewsSerializer,
)
from .paginations import NewsPagination

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
    pagination_class = NewsPagination

    serializer_class = DomesticNewsSerializer

    def get_queryset(self):
        return DomesticNews.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

        try:
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)
        except:
            chromedriver_autoinstaller.install(True)
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)

        driver.implicitly_wait(10)

        url = "https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258"

        driver.get(url)

        # 주제
        subject_elements = driver.find_elements(By.CSS_SELECTOR, '#contentarea_left > ul > li.newsList.top > dl > .articleSubject > a')

        # 언론사, 뉴스 날짜
        press_elements = driver.find_elements(By.CSS_SELECTOR, '#contentarea_left > ul > li.newsList.top > dl > .articleSummary > span.press')
        wdate_elements = driver.find_elements(By.CSS_SELECTOR, '#contentarea_left > ul > li.newsList.top > dl > .articleSummary > span.wdate')

        for i in range(len(subject_elements)-1, -1, -1):
            object, is_created = DomesticNews.objects.get_or_create(
                title=subject_elements[i].text,
                url=subject_elements[i].get_attribute('href'),
                press=press_elements[i].text,
                date=wdate_elements[i].text,
            )
            object.save()

        driver.implicitly_wait(10)
        driver.quit()

        return Response(status=status.HTTP_201_CREATED)
    

class OverseasNewsView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    pagination_class = NewsPagination

    serializer_class = OverseasNewsSerializer

    def get_queryset(self):
        return OverseasNews.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

        try:
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)
        except:
            chromedriver_autoinstaller.install(True)
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)

        driver.implicitly_wait(10)

        url = "https://finance.naver.com/news/news_list.naver?mode=LSS3D&section_id=101&section_id2=258&section_id3=403"

        driver.get(url)

        # 주제
        subject_elements = driver.find_elements(By.CSS_SELECTOR, '#contentarea_left > ul > li.newsList.top > dl > .articleSubject > a')

        # 언론사, 뉴스 날짜
        press_elements = driver.find_elements(By.CSS_SELECTOR, '#contentarea_left > ul > li.newsList.top > dl > .articleSummary > span.press')
        wdate_elements = driver.find_elements(By.CSS_SELECTOR, '#contentarea_left > ul > li.newsList.top > dl > .articleSummary > span.wdate')

        for i in range(len(subject_elements)-1, -1, -1):
            object, is_created = OverseasNews.objects.get_or_create(
                title=subject_elements[i].text,
                url=subject_elements[i].get_attribute('href'),
                press=press_elements[i].text,
                date=wdate_elements[i].text,
            )
            object.save()

        driver.implicitly_wait(10)
        driver.quit()

        return Response(status=status.HTTP_201_CREATED)
