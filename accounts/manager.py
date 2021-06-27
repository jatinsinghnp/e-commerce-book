

from django.contrib.auth.base_user import BaseUserManager

class ShopUserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('you must have email ')
        if not username:
             raise ValueError('yo must have user name')
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,username,email,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password

        )

        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user
        
