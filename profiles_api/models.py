from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.conf import settings

# Create your models here.

class UserProfileManager(BaseUserManager):
    """ manager for user profile"""
    def create_user(self,email,name,password=None):
        """ create new user profile"""
        if not email:
            raise ValueError('User Must Have An Email Address')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        """Create and save a new Superuser with given detail"""
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


class User_Profile(AbstractBaseUser,PermissionsMixin):
    """
    database model for users in the system
    """
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects =UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        retrive full name of user
        :return:
        """
        return self.name
    def get_short_name(self):
        """
        retrive short name of user
        :return:
        """
        return self.name


    def __str__(self):
        """ return string represtentation of our user"""
        return self.email

class snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)


    def __str__(self):
        return self.title


class ProfileFeedItem(models.Model):
    """Profile status Update"""
    user_profile=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text=models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model a string"""
        return self.status_text