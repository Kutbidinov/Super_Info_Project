from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from django.views.generic import TemplateView
from blog.models import Publication, PublicationComment, ClientContact
from blog.telegram_bot import bot

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            "publication_list": Publication.objects.all(),
            "hashtags": Publication.objects.all(),
            'publication_list': Publication.objects.filter(is_active=True)

        }
        return context





class ContactView(TemplateView):
    template_name = 'contact.html'





class PublicationDetailView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        context = {
            "publication": Publication.objects.get(id=publication_pk)
        }
        return context



class CreatePublicationCommentView(View):

    def post(self, request, *args, **kwargs):
        publication_pk = kwargs['pk']
        publication = Publication.objects.get(id=publication_pk)

        comment_text = request.POST['comment_text']

        PublicationComment.objects.create(publication=publication, text=comment_text)
        bot.send_message(chat_id=123456789, text='Вашей публикации доступен Сообщения: Не забудьте  проверить!')

        return redirect('publication-detail', pk=publication_pk)



def client_contact_create_view(request):
    print("Данные о ПОСТ запроса!",  request.POST)
    name = request.POST.get("name")
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    ClientContact.objects.create(name=name, email=email,  subject=subject, message=message)
    return HttpResponse('<h1> Ваше сообщения! </h1>')





