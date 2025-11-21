from django.db import models
from django.contrib import admin
class Car(models.Model):
    brand_name=models.CharField(max_length=20)
    CAR_name=models.CharField(max_length=18)
    enginenum=models.IntegerField()
    release_date=models.DateField()

class CarAdmin(admin.ModelAdmin):
    list_display=('brand_name', 'CAR_name', 'enginenum', 'release_date')
# Create your models here.
