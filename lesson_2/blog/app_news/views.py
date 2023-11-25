import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def news_list(request, *args, **kwargs):
    context = {
        'date_now': datetime.datetime.now(),
        'news_categories': ('Criminal', 'Politics', 'Sports')
    }
    return render(request, 'app_news/index.html', context=context)
