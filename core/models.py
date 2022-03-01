from typing_extensions import Self
from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User

# Create your models here.
ADMIN_USER_ID = 1

class product(models.Model):

    id = models.AutoField(primary_key=True)

    created_by = models.ForeignKey(User, default = ADMIN_USER_ID, on_delete=models.CASCADE)

    barcode_image = models.ImageField(upload_to="product_images", default = "default_shop_product", blank=True, null=True)
    cover_image = models.ImageField( upload_to="product_images", default = "default_shop_product", blank=True, null=True)
    label_image = models.ImageField( upload_to="product_images", default = "default_shop_product", blank=True, null=True)

    gazo_bango = models.IntegerField(default=0, null=True, blank=True)
    qr_bango = models.IntegerField(default=0, null=True, blank=True)

    kensa_bango = models.IntegerField(blank=True, null = True)
    kensa_id = models.IntegerField(blank=True, null = True)

    shouhinmei = models.CharField(max_length=60, null=True, blank = True)

    status = models.IntegerField(default=0)
    
    image_similarity_checked = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return str(self.created_by.username) + str(id)