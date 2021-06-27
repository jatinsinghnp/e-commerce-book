
from unicodedata import normalize
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .manager import ShopUserManager
# Create your models here.






class ShopUser(AbstractBaseUser,PermissionsMixin):
   first_name=models.CharField(max_length=220,db_index=True)
   last_name=models.CharField(max_length=220,db_index=True)
   username=models.CharField(max_length=250,unique=True,blank=False,null=False)
   phone_number=models.CharField(max_length=10)
   email=models.EmailField(unique=True,max_length=200)
    # Required field
   is_active=models.BooleanField(default=False)
   is_admin=models.BooleanField(default=False)
   is_staff=models.BooleanField(default=False)
   join_date=models.DateTimeField(auto_now_add=True)
   last_login=models.DateTimeField(auto_now_add=True)
   is_superadmin=models.BooleanField(default=False)
   USERNAME_FIELD='email'
   REQUIRED_FIELDS=['username','first_name','last_name']

   objects=ShopUserManager()

   
   def __str__(self):
       return self.first_name

    
   def has_perm(self,perm,obj=None):
        return self.is_admin

   def has_module_perms(self,add_lable):
       return True
