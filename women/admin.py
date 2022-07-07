from django.contrib import admin

from .models import Category, Women


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'time_create', 'time_updated', 'is_published', 'cat', 'user')

