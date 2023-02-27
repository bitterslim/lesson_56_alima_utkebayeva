from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Product name')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Description')
    image = models.CharField(max_length=500, null=False, verbose_name='Image')
    category = models.CharField(max_length=100, null=False, blank=False, verbose_name='Category')
    leftover = models.PositiveIntegerField(null=False, verbose_name= 'Leftover')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')