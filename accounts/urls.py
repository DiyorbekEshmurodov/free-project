from django.urls import path
from .views import *
urlpatterns = [
    path('',main_account,name='home'),
    path('dashboard/',index_page,name='index'),
    path('login/',login_page,name='login_page'),
    path('logout/',logout_page,name='logout_page'),
]
