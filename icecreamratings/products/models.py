from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    slug = models.SlugField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField()

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.product_name

class Color(models.Model):
    color_name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=15,null=True,blank=True)
    def __str__(self):
        return self.color_name

class Size(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    



class Variation(models.Model):
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    colors = models.ForeignKey(Color,on_delete=models.CASCADE)
    sizes = models.ForeignKey(Size,on_delete=models.CASCADE)
    is_available = models.BooleanField()
    
    def __str__(self):
        return self.products.product_name







