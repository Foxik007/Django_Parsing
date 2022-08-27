import json

from django.contrib.auth import logout
from django.shortcuts import render
from rest_framework.views import APIView

from .models import News
from rest_framework import viewsets, filters, generics

from .serializers import NewsSerializer, NewsTagSerializer


def save_data_yandex(request):
    file = open("parsing/yandex_json/article_yandex.json", 'r')  # Предположим это json
    data = json.loads(file.read())  # Загружаем json
    file.close()
    for row in data:
        News.objects.update_or_create(name=row['name'],
                                      description=row['description'],
                                      tags=row['tags'],
                                      tag_news=row['tag_news'],
                                      date=row['date'])  # Название модели и полей надеюсь вы сами подставите
    return render(request, 'index.html')


def save_data_ozon(request):
    file = open("parsing/ozon_json/article_ozon.json", 'r')  # Предположим это json
    data = json.loads(file.read())  # Загружаем json
    file.close()
    for row in data:
        News.objects.update_or_create(name=row['name'],
                                      description=row['description'],
                                      tags=row['tags'],
                                      tag_news=row['tag_news'],
                                      date=row['date'])  # Название модели и полей надеюсь вы сами подставите
    return render(request, 'index.html')


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']


class NewsTagNewsViewSet(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsTagSerializer
    name = 'tag_news'
    search_fields = (
        'tag_news',
    )


class NewsTagViewSet(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsTagSerializer
    name = 'tags'
    search_fields = (
        'tags',
    )
