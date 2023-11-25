from django.urls import path

from classWork.lesson_2.blog.app_news.views import news_list

urlpatterns = [
    path('', news_list, name='news_list')
]