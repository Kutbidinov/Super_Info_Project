"""
URL configuration for super_info_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog.views import HomeView, ContactView, PublicationDetailView, CreatePublicationCommentView, client_contact_create_view, HomeSearchView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]



urlpatterns += i18n_patterns (
    path('home/', HomeView.as_view(), name='home_url'),
    path('home/search/', HomeSearchView.as_view(), name='home-search-url'),
    path('contact/', ContactView.as_view(), name='contact_url'),
    path('publication_detail/<int:pk>', PublicationDetailView.as_view(), name='publication_detail_url'),
    path('publication-detail/<int:pk>/create-comment/', CreatePublicationCommentView.as_view(), name='create_comment_url'),
    path('home/client-contact-create/', client_contact_create_view, name='client_contact_create')


)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




