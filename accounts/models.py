from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    # Django'ning tayyor User modeli bilan One-to-One bog'lash
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profil')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    buyi = models.CharField(max_length=100, null=True, blank=True)
    vazni = models.CharField(max_length=100, null=True, blank=True)
    jinsi = models.CharField(max_length=100, null=True, blank=True)
    maqsadi = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Profili"


