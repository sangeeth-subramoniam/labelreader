from email.mime import image
from venv import create
from django.shortcuts import redirect, render


from django.views.decorators.csrf import csrf_exempt
from numpy import save
from core.models import product

from .forms import productinstanceform

import os
import base64
from django.core.files.base import ContentFile

#DEPENDENCIES
import cv2



# Create your views here.
def home(request):
    if request.user.is_authenticated:
        curruser = request.user

        product_instance,created = product.objects.get_or_create(
            created_by = request.user,
            status = 0,
            
            defaults={
                'barcode_image' : None,
                'cover_image' : None,
                'label_image' : None,
                'kensa_bango' : None,
                'kensa_id' : None,
                'shouhinmei' : None,
            }
        )

        print('instance created is ', product_instance , created)

        return render(request,'landing/homepage.html',{'curr_user' : curruser, 'productinstance' : product_instance})
    else:
        return redirect('authentication:signin')

def camera(request,mode):
    if request.user.is_authenticated:
        curruser = request.user

        productinstance = product.objects.get(created_by = request.user , status = 0)

        context = {
            'cameraclick' : 1 ,
            'FoodCheck' : 1 ,
            'userid' : curruser.id,
            'result_img1' : 'TEST/IMAGE/PATH',
            'camera_mode' : mode,
            'productinstance' : productinstance
        }
        
        return render(request,'camera.html', context)
    
    else:

        return redirect('authentication:signin')

@csrf_exempt
def tester(request):

    if request.method == "POST":

        current_product_instance = product.objects.get(created_by = request.user, status = 0)

        form = productinstanceform(request.POST, request.FILES)

        if form.is_valid():
            camera_mode = form.cleaned_data.get("camera_mode")
            count = form.cleaned_data.get("count")
            img_base64 = request.POST.get('img_data')
            
            if camera_mode == "barcode":
                
                format, imgstr = img_base64.split(';base64,') 
                ext = format.split('/')[-1] 

                data = ContentFile(base64.b64decode(imgstr))  
                file_name = str(current_product_instance.id) + str(request.user.username) + str('_barcode.') + ext

                current_product_instance.barcode_image.save(file_name,data, save=True)

            else:

                format, imgstr = img_base64.split(';base64,') 
                ext = format.split('/')[-1] 

                data = ContentFile(base64.b64decode(imgstr))  
                file_name = str(current_product_instance.id) + str(request.user.username) + str('_hyoushi.') + ext

                current_product_instance.cover_image.save(file_name,data, save=True)

            current_product_instance.save()

        else:
            print(form.errors)
            print('Form is not valid')

        return redirect('homepage:home')
    
    else:
        print('GET REQUEST')
        return redirect('homepage:home')


def remove_barcode(request):

    print('remove barcode')
    current_product_instance = product.objects.get(created_by = request.user, status = 0)
    current_product_instance.barcode_image = None
    current_product_instance.save()

    return redirect('homepage:home')


def remove_hyoushi(request):

    print('remove hyoushi')
    current_product_instance = product.objects.get(created_by = request.user, status = 0)
    current_product_instance.cover_image = None
    current_product_instance.save()

    return redirect('homepage:home')


def register_check(request,bcode=0,coverimage=0):

    print('check based on uploadded barcode and cover before register')

    print('Bcode and cover image are ', bcode, coverimage)

    return redirect('https://www.google.com')

