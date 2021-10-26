from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    image = models.ImageField()
    description = models.TextField(max_length=4000)
    prise = models.IntegerField(default=0)
    sale = models.IntegerField(default=0 , null=True , blank = True)
    @property
    def imgUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    contact = models.CharField(max_length=11)
    num_meters = models.IntegerField(default=0)
    product = models.ForeignKey(Product,related_name='product',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='product',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    sale_me = models.ForeignKey(Product , related_name='mysale',null=True , blank=True ,on_delete=models.CASCADE)
    complete = models.BooleanField(default=False, null=True, blank=False)


class Man(models.Model):
    name = models.CharField(max_length=40,null=True)
    contact = models.CharField(max_length=11,unique=True,null=True)
    address = models.CharField(max_length=300,unique=True,null=True)
    salary = models.IntegerField(default=0,null=True)