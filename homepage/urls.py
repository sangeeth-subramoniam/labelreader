from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'homepage'
urlpatterns = [
    path('', views.home , name = "home"),
    path('camera', views.camera , name = "camera"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
