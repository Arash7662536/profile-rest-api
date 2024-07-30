from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """manager for user profile"""

    def creat_user(self,email,name,password=None):
        """creat a new user profile """
        if not email:
            raise ValueError("User must have an Email Address!!")
        email=self.normalize_email(email)
        user=self.model(name=name,email=email)

        user.set_password(password)

        user.save(using=self._db)
        return User

    def creat_superuser(self,email,name,password):
        """ Create and save a new superuser with given details """
        self.creat_user(email,name,password)


        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    # """docstring fs UserProfile.AbstractBaseUser,PermissionsMixindef __init__(self, arg):
    #     sups UserProfile,AbstractBaseUser,PermissionsMixin.__init__()
    #     self.arg = arg

        email=models.EmailField(max_length=225,unique=True)
        name=models.CharField(max_length=225)
        is_active=models.BooleanField(default=True)
        is_staff=models.BooleanField(default=False)


        objects=UserProfileManager()

        USERNAME_FIELD = "email"
        REQUIRED_FIELD= ["name"]


        def get_full_name(self):
            """Retirive Full name """

            return self.name

        def get_short_name(self):
            """ retrive short name of user"""
            return self.name


        def __str__(self):
            """ return string represention of user """
            return self.email


# Create your models here.
