from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=100)  # Adjust max_length as needed
    date = models.DateField()  # Stores only the date (year, month, day)

    def __str__(self):
        return self.name 
