from django.db import models

# Create your models here.


class User(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    photo = models.TextField()
    password = models.CharField(max_length=150)


