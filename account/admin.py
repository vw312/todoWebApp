from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import myUser

admin.site.register(myUser, UserAdmin)
