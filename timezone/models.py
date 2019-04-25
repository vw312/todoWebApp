from django.db import models

# Create your models here.
class timezone (models.Model):
    timezone=models.CharField(max_length=100 ,blank=False)
