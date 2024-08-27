from django import forms
from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from blog.models import Publication, Category, Hashtag, PublicationComment, ClientContact



@admin.register(Publication)
class PublicationAdmin(TranslationAdmin):
    list_display = ['title']

    # description_ru = forms.CharField(label="Описания", widget=CKEditorUploadingWidget())
    # description_ky = forms.CharField(label="Описания", widget=CKEditorUploadingWidget())
    #
    #

@admin.register(Hashtag)
class HashtadAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ["title"]


@admin.register(PublicationComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(ClientContact)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['email']
