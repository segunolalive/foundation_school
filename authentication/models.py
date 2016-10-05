import os, sys
from PIL import Image

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


from foundation_school import settings

class AccountManager(BaseUserManager):
    def create_user(self, email, first_name, password=None, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        account = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            )

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
        # return ' '.join([self.first_name, self.last_name])
        return self.first_name

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


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Profile(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    last_name = models.CharField(max_length=40, blank=True, null=True, default="not set")

    region = models.CharField(max_length=40, blank=True, null=True, default="not set")
    zone = models.CharField(max_length=40, blank=True, null=True, default="not set")
    church = models.CharField(max_length=40, blank=True, null=True,  default="not set")

    image_medium = models.CharField(max_length=255, blank=True)
    image_thumb = models.CharField(max_length=255, blank=True)

    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            )

    def __str__(self):
        return self.account.email

    def __unicode__(self):
        return self.account.email

    def save(self, *args, **kwargs):
        super(Profile, self).save()
        if self.image:
            sizes = {
            'thumbnail': {'height': 100, 'width': 100},
            'medium': {'height': 300, 'width': 300},}

            image_url = str(self.image.url)
            image_path = str(self.image.path)
            fullpath = os.path.split(image_path)[0]

            extension = image_url.rsplit('.', 1)[1]

            image_name = os.path.split(image_url)[1].rsplit('.', 1)[0]
            image_rel_path = os.path.split(image_url)[0]

            im = Image.open(image_path)

            # create medium image
            im.thumbnail((sizes['medium']['width'], sizes['medium']['height']), Image.LANCZOS)
            medname = image_name + "_" + "medium" + ".jpg"
            im.save(os.path.join(fullpath, medname))
            # self.image_medium = (os.path.join(image_rel_path, medname))
            self.image_medium = image_rel_path + "/" + medname

            # create thumbnail image
            im.thumbnail((sizes['thumbnail']['width'], sizes['thumbnail']['height']), Image.LANCZOS)
            thumbname = image_name + "_" + "thumbnail" + ".jpg"
            im.save(os.path.join(fullpath, thumbname))
            # self.image_thumb = (os.path.join(image_rel_path, thumbname))
            self.image_thumb = image_rel_path + "/" + thumbname

            original_image_full_path = os.path.join(settings.BASE_DIR, self.image.path)
            os.remove(original_image_full_path)
            self.image = None

            super(Profile, self).save(*args, **kwargs)


@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(account=instance)

@receiver(post_save, sender=Account)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
