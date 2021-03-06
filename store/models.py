
from django.db import models
from django.urls import reverse
from .slugify import rand_slug
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=225)
    author_desc=models.TextField()
    def __str__(self):
        return self.name
    

class Category(models.Model):
    genres=models.CharField(max_length=200)
    cat_slug=models.SlugField(unique=True,max_length=225)
    def __str__(self):
        return self.genres


    def get_absolute_url(self):
        return reverse("store:category_list", args=[str(self.cat_slug)])
    
    



class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    book_title=models.CharField(max_length=200,unique=True,null=False,blank=False)
    isbn=models.BigIntegerField()
    book_desc=models.TextField()
    phone_number=models.BigIntegerField()
    pagenum=models.IntegerField()
    image=models.ImageField(upload_to='book/',default='no')

    def __str__(self):
        return self.book_title
    
    


class Product(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    prod_title=models.CharField(max_length=200,unique=True)
    prod_slug=models.SlugField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    prod_desc=models.TextField()
    prod_image=models.ImageField(upload_to='product/',default='emp')
    created_at=models.DateTimeField(auto_now_add=True)
    isavaliabe=models.BooleanField(default=True)

    def __str__(self):
        return self.prod_title

    


       
    def get_absolute_url(self):
        return reverse("store:product_detail", args=[str(self.prod_slug)])


ITEM_CHOICES=[
    ('Primary','Primary'),
    ('Secondary','Secondary'),
    



]

class Items(models.Model):
    item_title=models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False)
    item_price=models.DecimalField(max_digits=5,decimal_places=2)
    item_discount=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)

    
    item_category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    lable=models.CharField(max_length=220,choices=ITEM_CHOICES)
    slug=models.SlugField(max_length=220,unique=True,blank=True)
    
    
    def __str__(self):
        return self.item_title.prod_title

    class Meta:
        verbose_name = "Items"
        verbose_name_plural = "Items"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.item_title.prod_title)
        super(Items, self).save(*args, **kwargs)
    








    






