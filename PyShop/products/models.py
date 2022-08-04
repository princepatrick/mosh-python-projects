from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=1083)


class Offer(models.Model):
    offer = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    discount = models.FloatField()



