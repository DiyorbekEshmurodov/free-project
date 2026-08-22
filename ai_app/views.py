from django.shortcuts import render
from .services import ai_handler
from .models import UserQuestion
from .prompts import SECTION_MAP
# 1. BARCHA KARTALAR RO'YXATI UCHUN UNIVERSAL VIEW
def cards_list_view(request, section_name):
    section_data = SECTION_MAP.get(section_name)

    ctx = {
        'section_name': section_name,
        'title': section_data['title'],
        'subtitle': section_data['subtitle'],
        'questions': section_data['questions'],
    }
    return render(request, 'ai_app/cards.html', ctx)


# 2. TANLANGAN KARTA DETAIL KUNI UCHUN UNIVERSAL VIEW
def card_detail_view(request, section_name, question_id):
    section_data = SECTION_MAP.get(section_name)
    question_data = section_data['questions'].get(question_id)

    # 1. Tizimdagi userning ma'lumotlarini bazadan olamiz
    user_info = None
    if request.user.is_authenticated:
        user_info = UserQuestion.objects.filter(user=request.user).first()

    # Agar foydalanuvchi ma'lumotlari bo'lsa ularni, bo'lmasa standart qiymatlarni uzatamiz
    buyi = user_info.buyi if user_info and user_info.buyi else 170
    vazni = user_info.vazni if user_info and user_info.vazni else 70
    maqsadi = user_info.maqsadi if user_info and user_info.maqsadi else "Sog'lom turmush tarzi"

    card_title = question_data.get('title', '')
    card_desc = question_data.get('short_desc', '')

    full_prompt = (
        f"Mavzu: {card_title}\n"
        f"Tavsif: {card_desc}\n"
        f"Foydalanuvchi ko'rsatkichlari: Bo'yi: {buyi} sm, Vazni: {vazni} kg, Maqsadi: {maqsadi}.\n\n"
        f"Vazifa: Ushbu foydalanuvchiga tanlangan mavzu bo'yicha uning ko'rsatkichlariga mos amaliy va aniq maslahat bering."
    )

    ai_result = ai_handler(full_prompt)

    ctx = {
        'section_name': section_name,
        'question_data': question_data,
        'ai_result': ai_result,
    }
    return render(request, 'ai_app/card_detail.html', ctx)
# from django.shortcuts import render
# from .models import UserQuestion
# from .forms import UserForm
# from .services import ai_handler
# from .prompts import *
#
# def nutrition_secrets_view(request):
#     return render(request, 'ai_app/nutrition_secrets.html', {'questions':NUTRITION_QUESTIONS})
#
#
# def nutrition_detail_view(request, question_id):
#     question_data = NUTRITION_QUESTIONS.get(question_id)
#     prompt_text = get_nutrition_question_prompt(question_id)
#     ai_result = ai_handler(prompt_text)
#
#     ctx = {
#         'question_data': question_data,
#         'ai_result': ai_result,
#     }
#     return render(request, 'ai_app/nutrition_detail.html', ctx)
#
# def ai_analysis_view(request):
#     return render(request, 'ai_app/ai_analysis.html', {'questions':AI_ANALYSIS_QUESTIONS})
#
# def ai_detail_view(request,question_id):
#     question_data = AI_ANALYSIS_QUESTIONS.get(question_id)
#     prompt_text = get_ai_analysis_prompt(question_id)
#     ai_result = ai_handler(prompt_text)
#     ctx = {
#         'question_data': question_data,
#         'ai_result': ai_result
#     }
#     return render (request, 'ai_app/ai_detail.html', ctx)
#
# def oqsil_view(request):
#     return render(request, 'ai_app/oqsil_view.html', {'questions':MACROS_QUESTIONS})
#
# def oqsil_detail_view(request, question_id):
#     question_data = MACROS_QUESTIONS.get(question_id)
#     prompt_text = get_oqsil_prompt(question_id)
#     ai_result = ai_handler(prompt_text)
#
#     ctx = {
#         'question_data': question_data,
#         'ai_result': ai_result
#     }
#     return render(request, 'ai_app/oqsil_detail.html', ctx)
#
# def diyetolog_view(request):
#     return render(request, 'ai_app/diyetolog_view.html', {'questions': ADVICE_QUESTIONS})
#
# def diyetolog_detail_view(request, question_id):
#     question_data = ADVICE_QUESTIONS.get(question_id)
#     prompt_text = get_diyetolog_prompt(question_id)
#     ai_result = ai_handler(prompt_text)
#     ctx = {
#         'question_data': question_data,
#         'ai_result': ai_result
#     }
#     return render(request, 'ai_app/diyetolog_detail.html', ctx)