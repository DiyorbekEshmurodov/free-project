from django.urls import path
from .views import *
from accounts.views import main_account

urlpatterns = [
    path('', main_account, name='main_account'),

    path('user_list/',plan_list,name='user_list'),
    path('user_create/',plan_create,name="user_create"),
    path('user_edit/<int:pk>/',plan_edit,name="user_edit"),
    path('user_delete/<int:pk>/',plan_delete,name="user_delete"),
]