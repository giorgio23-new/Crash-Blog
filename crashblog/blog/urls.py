from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog'
urlpatterns = [
    path('search/', views.SearchListView.as_view(), name='search'),
    path('<slug:category_slug>/<slug:slug>', views.PostDetailsView.as_view(), name='post_details'),
    path('<slug:slug>/', views.CategoryListView.as_view(), name='categories'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
