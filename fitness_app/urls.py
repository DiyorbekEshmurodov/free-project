from django.urls import path
from .views import get_place, home_page, hisobot_create

urlpatterns = [
    path('',home_page,name='home_page'),
    path('hisobot',hisobot_create,name='hisobot_list'),
    path('user_place/', get_place, name='user_place')
]