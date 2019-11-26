from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'date', 'author') 
    list_editable = ('title',)
    list_display_links = ('date',)
    list_filter = ('date',)
    search_fields = ('title', 'body',)
