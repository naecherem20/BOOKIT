from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id , filename)

class Category(models.Model):
    title=models.CharField( max_length=100)
    deparment=models.TextField(max_length=200)
    banner=models.ImageField(default="fallback.png",blank=True, upload_to="category", height_field=None, width_field=None, max_length=None)
    
    class Meta:
        verbose_name_plural="categories"

    def __str__(self):
        return self.title

class Vendor(models.Model):
    first_name=models.CharField( max_length=100)
    last_name=models.TextField(max_length=200)
    banner=models.ImageField(default="fallback.png",blank=True, upload_to="user_directory_path", height_field=None, width_field=None, max_length=None)
    address=models.CharField(max_length=100,default="Nigeria")
    bio=models.CharField(max_length=100,blank=True)
    contact=models.CharField(max_length=100,default="+234 (000) 678")
    response_duration=models.CharField(default='typically replies within an hour',max_length=100)
    shipping_time=models.FloatField(default="very fast", max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="vendors"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    title=models.CharField( max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    item=models.TextField(max_length=200)
    banner=models.ImageField(default="fallback.png",blank=True, upload_to="uploads/product/", height_field=None, width_field=None, max_length=None)
    product_description=models.CharField(max_length=100,blank=True)
    contact=models.CharField(max_length=100,default="+234 (000) 678")
    price=models.DecimalField(default='0.00',decimal_places=2,max_digits=9)
    shipping_time=models.CharField(default="very fast", max_length=100)
    
    #add sales
    on_sales=models.BooleanField(default=False)
    sales_price=models.DecimalField(default='0.00',decimal_places=2,max_digits=9)
    

    class Meta:
        verbose_name_plural="products"

    def __str__(self):
        return self.title

class Order(models.Model):
    vendor=models.ForeignKey( Vendor,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.vendor
