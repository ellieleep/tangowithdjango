from django.contrib import admin

from .models import Page
from .models import Category


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'views', 'likes']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
