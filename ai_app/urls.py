from django.urls import path
from .views import *
from accounts.views import index_page

urlpatterns = [

    path('dashboard/',index_page,name='index'),
    path('<str:section_name>/', cards_list_view, name='cards_list'),
    path('<str:section_name>/<str:question_id>/', card_detail_view, name='card_detail')

    # path('nutrition-secrets/',nutrition_secrets_view, name='nutrition_secrets'),
    # path('nutrition-secrets/<str:question_id>/', nutrition_detail_view, name='nutrition_detail'),
    #
    # path('ai_analysis/',ai_analysis_view, name='ai_analysis'),
    # path('ai_analysis/<str:question_id>/', ai_detail_view, name='ai_detail'),
    #
    # path('oqsil_view/',oqsil_view, name='oqsil'),
    # path('oqsil_view/<str:question_id>/',oqsil_detail_view, name='oqsil_detail'),
    #
    # path('diyetolog_view/',diyetolog_view, name='diyetolog'),
    # path('diyetolog_view/<str:question_id>/',diyetolog_detail_view, name='diyetolog_detail'),
]