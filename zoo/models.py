from django.db import models

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    area = models.IntegerField()
    floors = models.IntegerField()

class Enclosure(models.Model):
    enclosure_id = models.AutoField(primary_key=True)
    square_foot = models.PositiveIntegerField()
    building_id = models.ForeignKey('Building', on_delete=models.CASCADE)
    