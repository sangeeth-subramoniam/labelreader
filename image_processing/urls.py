from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'image_processing'
urlpatterns = [
    path('', views.image_similarity , name = "image_similarity"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)