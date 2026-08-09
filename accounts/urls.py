from django.urls import path
from .views import *
urlpatterns = [
    path('',main_account,name='main_account'),
    path('login/',login_page,name='login_page'),
    path('logout/',logout_page,name='logout_page'),
]
