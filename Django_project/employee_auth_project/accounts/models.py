from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

class CustomUserManager(BaseUserManager):

    def create_user(self, email =None, password = None,full_name=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
    
        email= self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using= self._db)
        return user
       
    def create_superuser(self,email,full_name,password,**other_fields):
        other_fields.setdefault("is_staff",True)
        other_fields.setdefault("is_superuser",True)
        other_fields.setdefault("is_active",True)

        if other_fields.get("is_staff")is not True:
            raise ValueError("Superuser must be staff")
        if other_fields.get("is_superuser")is not True:
            raise ValueError("is_superuser should be true to create superuser")
        
        return self.create_user(email,password,full_name,**other_fields)
    
class Employee(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    full_name= models.CharField(max_length=30)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    date_joined= models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    objects= CustomUserManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["full_name"]


    def __str__(self):
        return self.email