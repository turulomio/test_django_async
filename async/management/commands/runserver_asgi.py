from django.core.management.base import BaseCommand
from os import system

class Command(BaseCommand):
    help = 'Runserver with asgi support using uvicorn'
        #Generate fixtures
                
    def handle(self, *args, **options):
        system("uvicorn test_django_async.asgi:application --reload --host 127.0.0.1 --port 8000")

