from django.db import models
from django.contrib.admin import widgets
from datetime import datetime,timedelta
import pytz

from account.models import myUser
from timezone.models import timezone

# Create your models here.
class Schedules(models.Model):
    user = models.ForeignKey(myUser, on_delete=models.CASCADE)
    what_todo=models.CharField(max_length=100,verbose_name="Event",blank=False)
    description=models.TextField(blank=True,verbose_name='Description')
    date_time=models.DateTimeField(verbose_name='When should i remind you ? ',blank=False) #this is offset naive
    state_user=models.BooleanField(verbose_name="Done ?",default=False)#this can be edited by the user
    state_db=models.BooleanField(default=False) #this used by django to grey out incomplete schedules which have expired(True means they should be greyed out)
    email_sent=models.BooleanField(default=False) #if email has been sent once it won't send again. Never exposed to user

    def get_absolute_url(self):
        return reverse("schedule",kwargs={"schedule_id":self.id})

    def update(self):
        target_user=myUser.objects.get(id=self.user_id)
        tz=pytz.timezone(target_user.get_timezone())

        #localizing stuff to user's timezone
        datetime_now=datetime.now(tz)
        schedule_datetime=tz.localize(self.date_time)
        if schedule_datetime < datetime_now:
            if not self.state_user and not  self.state_db:
                self.state_db=True
                self.save()

    def email (self):
        target_user=myUser.objects.get(id=self.user_id)
        tz=pytz.timezone(target_user.get_timezone())

        #localizing stuff to user's timezone
        datetime_now=datetime.now(tz)
        schedule_datetime=tz.localize(self.date_time)
        if schedule_datetime>=datetime_now or schedule_datetime<datetime_now+timedelta(hours=2)  :
            target_user.email_user("From Mighty_Maharaja's todoWebApp","You have a job to do in a few hours.\nLogin to your account to know more.",
                                                                                                from_email="todo@todoWebApp.com")
            self.email_sent=True
            self.save()
