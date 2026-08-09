from django.db import models
from accounts.models import UserDetail

class FitnessPlan(models.Model):
    kunlik = models.TextField(max_length=255,null=True,blank=True)
    haftalik = models.TextField(max_length=255,null=True,blank=True)
    oylik = models.TextField(max_length=255,null=True,blank=True)
    yillik = models.TextField(max_length=255,null=True,blank=True)
    goal = models.TextField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(UserDetail,blank=True,null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.kunlik},{self.haftalik},{self.oylik},{self.yillik},{self.created_at}"

