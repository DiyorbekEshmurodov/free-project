from django.db import connection
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

def get_kun():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM app_kunlik""")
        kun = dictfetchall(cursor)
        return kun

def get_haftalik():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM app_haftalik""")
        haftalik = dictfetchall(cursor)
        return haftalik

def get_oylik():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM app_oylik""")
        oylik = dictfetchall(cursor)
        return oylik

def get_yillik():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM app_yillik""")
        yillik = dictfetchall(cursor)
        return yillik

def get_all_hisobot():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM app_hisobot""")
        hisobot = dictfetchall(cursor)
        return hisobot

