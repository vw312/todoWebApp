from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.urls import reverse

from timezone.models import timezone
# Create your models here.
class myUserManager (UserManager):
    pass

class myUser(AbstractUser) :
    timezone=models.ForeignKey(timezone,on_delete=models.CASCADE,default=588)
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    def get_absolute_url(self):
        return reverse("profile",kwargs={"user_id":self.id})

    def get_timezone(self):
        """Returns a string denoting the user's timezone"""
        timezone_obj=timezone.objects.get(id=self.timezone_id)
        return timezone_obj.timezone  
