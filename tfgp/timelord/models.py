from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class Category(models.Model):
    max_l1 = 50
    name = models.CharField(max_length=max_l1, unique=True)
    description = models.CharField(max_length=250)
    colour = models.CharField(max_length = 20)
    ownerUsername = models.CharField(max_length = max_l1)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.description

    def __unicode__(self):
        return self.description
