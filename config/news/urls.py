from django.urls import include, path
from rest_framework import routers

from . import views
from .views import save_data_yandex, save_data_ozon, NewsTagViewSet

router = routers.DefaultRouter()
router.register(r'api/news', views.NewsViewSet)

urlpatterns = [
    path('api/tags_news', views.NewsTagNewsViewSet.as_view()),
    path('api/tags', views.NewsTagViewSet.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('json_yandex/', save_data_yandex),
    path('json_ozon/', save_data_ozon),
]
