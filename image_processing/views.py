from email.mime import image
from django.shortcuts import redirect, render

from static.dependancy import Annoy,Barcode

from core.models import product

# Create your views here.

def barcode_comparison(product_instance):

    image_path_of_file = str(product_instance.barcode_image.file)

    image_path_of_file_filename = str(image_path_of_file).split('\\')[-1]

    image_directory = r'C:\\Users\\s-sangeeth-k\\Desktop\\django\\labelreader\\media\\product_images\\'

    path_file = str(image_directory) + str(image_path_of_file_filename)

    related_barcode = Barcode.BarcordRead(path_file)

    print(related_barcode)

    return related_barcode



def image_similarity(product_instance):    

    #ANNOY

    #base_media = r'C:\\Users\\s-sangeeth-k\\Desktop\\django\\labelreader'
    #image_path = os.path.join(base_media,product_instance.cover_image.url) 
    #image_path = r'C:\\Users\\s-sangeeth-k\\Desktop\\django\\labelreader\\media\\product_images\\3sangeeth_hyoushi_hKJM0V4.png'
    #image_path = product_instance.cover_image.url
    
    image_path_of_file = str(product_instance.cover_image.file)

    image_path_of_file_filename = str(image_path_of_file).split('\\')[-1]

    image_directory = r'C:\\Users\\s-sangeeth-k\\Desktop\\django\\labelreader\\media\\product_images\\'

    path_file = str(image_directory) + str(image_path_of_file_filename)

    ruigi_img = Annoy.Ruigi_Img(path_file)

    print('similar images are ', ruigi_img)
    


    #check for images with gazo number 32,84,22 and show their value

    related_images = product.objects.all().filter(gazo_bango__in = ruigi_img[0], status = 1, image_similarity_checked = 1 )

    return related_images

    print(related_images)
    print('the instance is ', product_instance)

    context = {
        'productinstance' : product_instance,
        'related_images' : related_images

    }

    return render(request, 'landing/homepage.html', context)