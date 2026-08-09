from django.db import models

class UserQuestion(models.Model):
    buyi = models.CharField(max_length=100, null=False, blank=False)
    vazni = models.CharField(max_length=100, null=False, blank=False)
    goal = models.CharField(max_length=100, null=False, blank=False)

