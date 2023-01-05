from django.db import models

# Create your models here.

class Name(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Hall(models.Model):
    Name = models.CharField(max_length=150)
    Size = models.CharField(max_length=4)
    Location= models.CharField(max_length=30)
    Description= models.CharField(max_length=30)
