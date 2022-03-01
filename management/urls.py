from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'management'
urlpatterns = [
    path('', views.search , name = "search"),
    path('search_form_action', views.search_form_action , name = "search_form_action"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)