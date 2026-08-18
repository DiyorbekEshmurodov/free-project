from django.shortcuts import render
from .models import UserQuestion
from .forms import UserForm
from .services import ai_handler
from .prompts import *

def nutrition_secrets_view(request):
    return render(request, 'ai_app/nutrition_secrets.html', {'questions':NUTRITION_QUESTIONS})


def nutrition_detail_view(request, question_id):
    question_data = NUTRITION_QUESTIONS.get(question_id)
    prompt_text = get_nutrition_question_prompt(question_id)
    ai_result = ai_handler(prompt_text=prompt_text)

    ctx = {
        'question_data': question_data,
        'ai_result': ai_result,
    }
    return render(request, 'ai_app/nutrition_detail.html', ctx)

def ai_analysis_view(request):
    return render(request, 'ai_app/ai_analysis.html', {'questions':AI_ANALYSIS_QUESTIONS})

def ai_detail_view(request,question_id):
    question_data = AI_ANALYSIS_QUESTIONS.get(question_id)
    prompt_text = get_ai_analysis_prompt(question_data)
    ai_result = ai_handler(prompt_text=prompt_text)
    ctx = {
        'question_data': question_data,
        'ai_result': ai_result
    }
    return render (request, 'ai_app/ai_detail.html', ctx)

def oqsil_view(request):
    return render(request, 'ai_app/oqsil_view.html', {'questions':MACROS_QUESTIONS})

def oqsil_detail_view(request, question_id):
    question_data = MACROS_QUESTIONS.get(question_id)
    prompt_text = get_oqsil_prompt(question_id)
    ai_result = ai_handler(prompt_text=prompt_text)

    ctx = {
        'question_data': question_data,
        'ai_result': ai_result
    }
    return render(request, 'ai_app/oqsil_detail.html', ctx)

def diyetolog_view(request):
    return render(request, 'ai_app/diyetolog_view.html', {'questions': ADVICE_QUESTIONS})

def diyetolog_detail_view(request, question_id):
    question_data = ADVICE_QUESTIONS.get(question_id)
    prompt_text = get_diyetolog_prompt(question_id)
    ai_result = ai_handler(prompt_text=prompt_text)
    ctx = {
        'question_data': question_data,
        'ai_result': ai_result
    }
    return render(request, 'ai_app/diyetolog_detail.html', ctx)