from django.db import models

class UserDetail(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=100,null=True,blank=True)
    buyi = models.CharField(max_length=100,null=False,blank=False)
    vazni = models.CharField(max_length=100,null=False,blank=False)
    jinsi = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


