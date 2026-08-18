from django.db import models
from accounts.models import UserDetail
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()



