from django.urls import path
from .views import *
from accounts.views import main_account

urlpatterns = [
    path('', main_account, name='main_account'),

    path('hisobot/', hisobot_list, name='hisobot_list'),
    path('hisobot/create/', hisobot_create, name='hisobot_create'),
    path('hisobot/edit/<int:pk>/', hisobot_edit, name='hisobot_edit'),
    path('hisobot/delete/<int:pk>/', hisobot_delete, name='hisobot_delete'),
]