from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'homepage'
urlpatterns = [
    path('', views.home , name = "home"),
    path('camera/<str:mode>', views.camera , name = "camera"),
    
    path('register_check/<int:bcode>/<int:coverimage>', views.register_check , name = "register_check"),

    path('tester', views.tester , name = "tester"),
    path('remove_barcode', views.remove_barcode , name = "remove_barcode"),
    path('remove_hyoushi', views.remove_hyoushi , name = "remove_hyoushi"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
