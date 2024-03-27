from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import BaseUserManager, AbstractUser

// This is our model file

ext_validator = FileExtensionValidator(['xlsx','pptx','docx'])

class admin_manager(BaseUserManager):
    def create_user(self, email, username, password=None, confirm_password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username = username,
            password = password,
           
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class adminLogin(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    objects = admin_manager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username','password']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

class FileUpload(models.Model):
    def uploadFiles(instance,filename):
        return '/'.join(['filesUploaded', str(instance.name), filename])
    
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to=uploadFiles, max_length=100,validators=[ext_validator])

class Signup(models.Model):
    Username = models.CharField(max_length=100)
    Email = models.EmailField(verbose_name="Email",max_length=255,unique=False,)
    Password = models.CharField(max_length=200)
    ConFirmPassword = models.CharField(max_length=200)
    is_Verified = models.BooleanField(default=True)


class Login(models.Model):
    Username = models.CharField(max_length=100)
    Email = models.EmailField(verbose_name="Email",max_length=255,unique=True,)
    Password = models.CharField(max_length=200)
    is_Verified = models.BooleanField(default=True)

