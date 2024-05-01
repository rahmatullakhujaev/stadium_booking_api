from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **kwargs):

        if not phone_number:
            raise ValueError("Users must have a phone number")

        user = self.model(
            phone_number=phone_number,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None):

        user = self.create_user(
            phone_number,
            '',
            password=password,

        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, null=False, blank=True)
    last_name = models.CharField(max_length=30, null=False, blank=True)
    username = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13, null=True, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number


class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Permission(models.Model):
    role = models.ManyToManyField(Role, related_name='roles')
    name = models.CharField(max_length=30)
    codename = models.CharField(max_length=200)

    def __str__(self):
        return self.name