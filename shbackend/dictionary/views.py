from django.shortcuts import render
from .models import Dictionary
from rest_framework import generics, mixins

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict


from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Create your views here.

# 단어 검색 ex. /dict?title='비상장'
class DictionarySearchView(APIView):
    def get(self, request, *args, **kwargs):
        
        dictionary = Dictionary.objects.all()
        titlename = request.query_params['title']

        if dictionary.filter(title = titlename).exists(): # 미리 저장해둔 DB에 있는 용어라면
        # if dictionary.filter(title__icontains = titlename).exists(): # 미리 저장해둔 DB에 있는 용어라면            
            # dictionary = dictionary.filter(title__contains = titlename)
            dictionary = dictionary.filter(title = titlename)

            ret = []
            for data in dictionary:
                ret.append({"content": data.content})
            
            return Response(ret)

        # else:
        #     return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            # 셀레니움
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

            try:
                driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)
            except:
                chromedriver_autoinstaller.install(True)
                driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)

            driver.implicitly_wait(10)

            url = "https://ko.dict.naver.com/#/main"
            driver.get(url)
            driver.implicitly_wait(10)

            element = driver.find_element(By.ID, "ac_input")
            element.send_keys(titlename)    #queryparams의 titlename 입력
            element.send_keys("\n")

            words = driver.find_elements(By.CSS_SELECTOR, '#searchPage_entry > div > div:nth-child(1) > ul > li > p span.u_word_dic')
            result_str = ""
            for e in words:
                result_str += (e.text + " ")

            return Response([{
                'title': titlename,
                'content': result_str,
            }], status=status.HTTP_200_OK)