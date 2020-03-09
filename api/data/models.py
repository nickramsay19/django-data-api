from django.db import models

# Create your models here.
class Person(models.Model):

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 20)
    ip_address = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name