from modeltranslation.translator import register, TranslationOptions
from blog.models import Category, Publication



@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)




@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('title', 'description')



