from django.urls import path
from .views import *

urlpatterns = [
    path('user_ask/',user_question_create,name='user_ask'),
]