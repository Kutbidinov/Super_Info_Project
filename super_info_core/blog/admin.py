from django.contrib import admin
from blog.models import Danislan


@admin.register(Danislan)
class DanislanAdmin(admin.ModelAdmin):
    list_display = ['name']
