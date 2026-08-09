from django.db import connection
from .models import FitnessPlan
from contextlib import closing

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns,row)) for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns,row))

def get_kun(user_id):
    """SELECT * FROM ? where user_id = %s"""
    try:
        return FitnessPlan.objects.filter(UserDetail_id=user_id).values().first()
    except FitnessPlan.DoesNotExist:
        return False

def get_haftalik(user_id):
    try:
        return FitnessPlan.objects.filter(UserDetail_id=user_id).values().first()
    except FitnessPlan.DoesNotExist:
        return False

def get_oylik(user_id):
    try:
        return FitnessPlan.objects.filter(UserDetail_id=user_id).values().first()
    except FitnessPlan.DoesNotExist:
        return False

def get_yillik(user_id):
    try:
        return FitnessPlan.objects.filter(UserDetail_id=user_id).values().first()
    except FitnessPlan.DoesNotExist:
        return False

def get_all_hisobot(user_id):
    hisobotlar = list(FitnessPlan.objects.filter(UserDetail_id=user_id).values())
    if not hisobotlar:
        return False
    return hisobotlar

