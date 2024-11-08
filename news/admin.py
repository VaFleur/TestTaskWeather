from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News, Place


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(News, NewsAdmin)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'coordinates', 'rating')
    search_fields = ('name',)
