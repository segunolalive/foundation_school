from django.db import models
from django.contrib.auth.models import (
BaseUserManager, AbstractBaseUser
)

class AccountManager(BaseUserManager):
    def create_user(self, email, first_name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        account = self.model(email=self.normalize_email(email),)
        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_superuser(self, email, first_name, password):
        """
        Creates and saves a User with the given email and password.
        """
        account = self.create_user(email, first_name, password=password)
        account.is_admin = True
        account.save(using=self._db)
        return account


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=40, blank=False, null=False)
    last_name = models.CharField(max_length=40, blank=True)

    region = models.CharField(max_length=40, blank=True)
    zone = models.CharField(max_length=40, blank=True)
    church = models.CharField(max_length=40, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',]

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
