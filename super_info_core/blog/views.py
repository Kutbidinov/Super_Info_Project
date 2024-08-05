from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Publication


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            "publication_list": Publication.objects.all()
        }
        return context



class ContactView(TemplateView):
    template_name = 'contact.html'


class PublicationDetailView(TemplateView):
    template_name = 'publication-detail.html'


