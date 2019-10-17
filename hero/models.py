from django.db import models


# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=(('M', 'Male'), ('F', 'Female')), default='F')
    movie = models.CharField(max_length=100)
    city = models.ForeignKey('City', related_name='heroes', on_delete=models.PROTECT, null=True)


class City(models.Model):
    name = models.CharField(max_length=100)
