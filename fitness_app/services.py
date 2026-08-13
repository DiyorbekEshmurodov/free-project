from .models import FitnessPlan

def get_plans_by_period(user_id, period):
    """
    Foydalanuvchi ID si va reja turiga (kunlik, haftalik, oylik, yillik)
    qarab ma'lumotlarni filtrlab beradi.
    """
    try:
        # UserDetail_id o'rniga Django'ning standart modeldagi user_id ishlatiladi
        plans = list(FitnessPlan.objects.filter(user_id=user_id, period_type=period).values())
        return plans if plans else False
    except Exception:
        return False

def get_all_hisobot(user_id):
    """
    Berilgan foydalanuvchining barcha turdagi reja va hisobotlarini olib keladi.
    """
    hisobotlar = list(FitnessPlan.objects.filter(user_id=user_id).values())
    if not hisobotlar:
        return False
    return hisobotlar


# from django.db import connection
# from .models import FitnessPlan
# from contextlib import closing
#
# def dictfetchall(cursor):
#     columns = [col[0] for col in cursor.description]
#     return [
#         dict(zip(columns,row)) for row in cursor.fetchall()
#     ]
#
# def dictfetchone(cursor):
#     row = cursor.fetchone()
#     if row is None:
#         return False
#     columns = [col[0] for col in cursor.description]
#     return dict(zip(columns,row))
#
# def get_kun(user_id):
#     """SELECT * FROM ? where user_id = %s"""
#     try:
#         return FitnessPlan.objects.filter(UserDetail_id=user_id).values().first()
#     except FitnessPlan.DoesNotExist:
#         return False
#
# def get_haftalik(user_id):
#     try:
#         return FitnessPlan.objects.filter(UserDetail_id=user_id).values().first()
#     except FitnessPlan.DoesNotExist:
#         return False
#
# def get_oylik(user_id):
#     try:
#         return FitnessPlan.objects.filter(UserDetail_id=user_id).values().first()
#     except FitnessPlan.DoesNotExist:
#         return False
#
# def get_yillik(user_id):
#     try:
#         return FitnessPlan.objects.filter(UserDetail_id=user_id).values().first()
#     except FitnessPlan.DoesNotExist:
#         return False
#
# def get_all_hisobot(user_id):
#     hisobotlar = list(FitnessPlan.objects.filter(UserDetail_id=user_id).values())
#     if not hisobotlar:
#         return False
#     return hisobotlar
#
