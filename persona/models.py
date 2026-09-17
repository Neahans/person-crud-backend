from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    image = models.ImageField(upload_to="persona/")

    def __str__(self):
        return self.name