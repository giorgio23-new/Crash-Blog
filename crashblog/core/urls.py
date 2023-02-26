from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(template_name='core/frontpage.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='core/about.html'), name='about'),
]

