from django.contrib import admin
from blog.models import Publication, Category, Hashtag, PublicationComment, ClientContact


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Hashtag)
class HashtadAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(PublicationComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(ClientContact)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['email']