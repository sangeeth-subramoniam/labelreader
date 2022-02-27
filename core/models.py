from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User

# Create your models here.
ADMIN_USER_ID = 1

class product(models.Model):

    id = models.AutoField(primary_key=True)

    created_by = models.ForeignKey(User, default = ADMIN_USER_ID, on_delete=models.CASCADE)

    barcode_image = ResizedImageField(size=[370, 530], upload_to="product_images", default = "default_shop_product", blank=True, null=True)
    cover_image = ResizedImageField(size=[370, 530], upload_to="product_images", default = "default_shop_product", blank=True, null=True)
    label_image = ResizedImageField(size=[370, 530], upload_to="product_images", default = "default_shop_product", blank=True, null=True)

    kensa_bango = models.IntegerField(blank=True, null = True)
    kensa_id = models.IntegerField(blank=True, null = True)

    shouhinmei = models.CharField(max_length=60, null=True, blank = True)

def __str__(self):
    return str(self.created_by.username) + str(id)