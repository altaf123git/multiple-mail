from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    field = models.CharField(max_length=30)
    college = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.first_name
    