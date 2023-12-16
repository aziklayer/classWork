from django.contrib import admin

from .models import News, Author


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at',
                    'activity_flag']
    lisf_filter = ['activity_flag']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


admin.site.register(News, NewsAdmin)
admin.site.register(Author, AuthorAdmin)

