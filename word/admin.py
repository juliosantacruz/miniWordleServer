from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    model=Category
    list_display=['name' ]


class WordAdmin(admin.ModelAdmin):
    model=Word
    list_display=['word','word_size' ,'category', 'created_at']
    search_fields=['word', 'category']

admin.site.register(Word, WordAdmin)
admin.site.register(Category, CategoryAdmin)