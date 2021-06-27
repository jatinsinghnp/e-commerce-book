from django.contrib import admin
from .models import Author,Book,Category,Product,Items
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['name','author_desc']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['author','book_title','pagenum','isbn']
    list_display_links=[]
    list_editable=['isbn','pagenum']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['genres']
    prepopulated_fields={
        'cat_slug':('genres',)
    }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['book','category','price','created_at','isavaliabe']
    list_display_links=[]
    list_editable=['isavaliabe','price']
    prepopulated_fields={
        'prod_slug':('prod_title',)
    }

@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    list_display=['item_title','lable','item_category']
    list_display_links=[]
    list_editable=['lable']
    
    