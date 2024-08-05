from django.contrib import admin
from blog.models import Publication, Category, Hashtag


@admin.register(Publication)
class DanislanAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Hashtag)
class HashtadAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]



