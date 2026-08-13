from django.db import models
from accounts.models import UserDetail

class FitnessPlan(models.Model):
    PERIOD_CHOICES = (
        ('daily', 'Kunlik'),
        ('weekly', 'Haftalik'),
        ('monthly', 'Oylik'),
        ('yearly', 'Yillik'),
    )
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Reja nomi")
    description = models.TextField(blank=True, null=True, verbose_name="Tavsif")
    period_type = models.CharField(max_length=10, choices=PERIOD_CHOICES, verbose_name="Turi")
    target_date = models.DateField(verbose_name="Sana")
    is_completed = models.BooleanField(default=False, verbose_name="Bajarildi")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title} ({self.period_type})"






# from django.db import models
# from accounts.models import UserDetail
#
# class FitnessPlan(models.Model):
#     kunlik = models.TextField(max_length=255,null=True,blank=True)
#     haftalik = models.TextField(max_length=255,null=True,blank=True)
#     oylik = models.TextField(max_length=255,null=True,blank=True)
#     yillik = models.TextField(max_length=255,null=True,blank=True)
#     goal = models.TextField(max_length=255,null=True,blank=True)
#     user = models.ForeignKey(UserDetail,blank=True,null=True,on_delete=models.SET_NULL)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.kunlik},{self.haftalik},{self.oylik},{self.yillik},{self.created_at}"
#
# class GetKunlik(models.Model):
#     kunlik = models.TextField(max_length=255,null=True,blank=True)
#     user = models.ForeignKey(UserDetail,blank=True,null=True,on_delete=models.SET_NULL)
#     create_at = models.DateTimeField(auto_now_add=True)
#
# class GetHaftalik(models.Model):
#     Dushanba = models.TextField(max_length=255,null=True,blank=True)
#     Seshanba = models.TextField(max_length=255,null=True,blank=True)
#     Chorshanba = models.TextField(max_length=255,null=True,blank=True)
#     Payshanba = models.TextField(max_length=255,null=True,blank=True)
#     Juma = models.TextField(max_length=255,null=True,blank=True)
#     Shanba = models.TextField(max_length=255,null=True,blank=True)
#     Yakshanba = models.TextField(max_length=255,null=True,blank=True)
#     user = models.ForeignKey(UserDetail,blank=True,null=True,on_delete=models.SET_NULL)
#     create_at = models.DateTimeField(auto_now_add=True)
#
# class GetOylik(models.Model):
#     Yanvar = models.TextField(max_length=255,null=True,blank=True)
#     Fevral = models.TextField(max_length=255,null=True,blank=True)
#     Mart = models.TextField(max_length=255,null=True,blank=True)
#     April = models.TextField(max_length=255,null=True,blank=True)
#     May = models.TextField(max_length=255,null=True,blank=True)
#     Iyun = models.TextField(max_length=255,null=True,blank=True)
#     Iyul = models.TextField(max_length=255,null=True,blank=True)
#     Avgust = models.TextField(max_length=255,null=True,blank=True)
#     Sentabr = models.TextField(max_length=255,null=True,blank=True)
#     Oktaybr = models.TextField(max_length=255,null=True,blank=True)
#     Noyabr = models.TextField(max_length=255,null=True,blank=True)
#     Dekabr = models.TextField(max_length=255,null=True,blank=True)
#     user = models.ForeignKey(UserDetail,blank=True,null=True,on_delete=models.SET_NULL)
#     create_at = models.DateTimeField(auto_now_add=True)
#
# class GetYillik(models.Model):
#     year_2026 = models.TextField(max_length=255,null=True,blank=True)
#     year_2027 = models.TextField(max_length=255,null=True,blank=True)
#     user = models.ForeignKey(UserDetail,blank=True,null=True,on_delete=models.SET_NULL)
#     create_at = models.DateTimeField(auto_now_add=True)
