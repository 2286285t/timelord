from django.contrib import admin

# Register your models here.

from timelord.models import UserAccount

admin.site.register(UserAccount)
