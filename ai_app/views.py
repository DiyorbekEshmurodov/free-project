from django.shortcuts import render
from .services import ai_handler
from .models import UserQuestion
from .prompts import SECTION_MAP
from accounts.models import UserDetail
# 1. BARCHA KARTALAR RO'YXATI UCHUN UNIVERSAL VIEW
def cards_list_view(request, section_name):
    section_data = SECTION_MAP.get(section_name)

    profil = None
    if request.user.is_authenticated:
        profil = UserDetail.objects.filter(user=request.user).first()

    ctx = {
        'section_name': section_name,
        'title': section_data['title'],
        'subtitle': section_data['subtitle'],
        'questions': section_data['questions'],
        'profil': profil,
        'has_profile': profil is not None,
    }
    return render(request, 'ai_app/cards.html', ctx)


# 2. TANLANGAN KARTA DETAIL KUNI UCHUN UNIVERSAL VIEW
def card_detail_view(request, section_name, question_id):
    section_data = SECTION_MAP.get(section_name)
    question_data = section_data['questions'].get(question_id)

    profil = None
    user_info = None
    if request.user.is_authenticated:
        profil = UserDetail.objects.filter(user=request.user).first()
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
        'profil': profil,
        'has_profile': profil is not None,
    }

    return render(request, 'ai_app/card_detail.html', ctx)
