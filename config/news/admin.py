from django.contrib import admin

# Register your models here.
from . import models
from .models import News

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name','tag_news',]
    save_as = True
    save_on_top = True

