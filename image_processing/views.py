from django.shortcuts import redirect, render

from static.dependancy import Annoy

from core.models import product

# Create your views here.

def image_similarity(request):

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

    #ANNOY

    host = 'svl14065-vm01'
    port= '5432'
    dbname = 'postgres'
    user = 'postgres'
    password = 'postgres'

    #base_media = r'C:\\Users\\s-sangeeth-k\\Desktop\\django\\labelreader'
    #image_path = os.path.join(base_media,product_instance.cover_image.url) 
    image_path = r'C:\\Users\\s-sangeeth-k\\Desktop\\django\\labelreader\\media\\product_images\\2sangeeth_hyoushi.png'

    print('image path is ', image_path)

    ruigi_img = Annoy.Ruigi_Img(host,port,dbname,user,password,image_path)

    print('similar images are ', ruigi_img)

    print(ruigi_img[0][0])
    print(ruigi_img[0][1])
    print(ruigi_img[0][2])

    #check for images with gazo number 32,84,22 and show their value

    return redirect('https://www.google.com')
