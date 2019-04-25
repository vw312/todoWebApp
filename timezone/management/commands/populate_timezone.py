from django.core.management.base import BaseCommand

from timezone.models import timezone

class Command(BaseCommand):
    help='Populates timezone database with timezones in timezones.txt'

    def handle(self,*args,**options):
        timezones=open('timezones.txt','r')
        for line in timezones:
            timezone.objects.create(timezone=line.strip()) #there is a newline character at the end of each timezone
        self.stdout.write(self.style.SUCCESS('Successfully populated timezone database'))
