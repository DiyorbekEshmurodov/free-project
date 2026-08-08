from django.db import models

class Hisobot(models.Model):
    kunlik = models.CharField(max_length=100,null=True,blank=True)
    haftalik = models.CharField(max_length=100,null=True,blank=True)
    oylik = models.CharField(max_length=100,null=True,blank=True)
    yillik = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.kunlik


class Place(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

