from django.shortcuts import render
from .models import UserQuestion
from .forms import UserForm
from .services import ai_handler

def user_question_create(request):
    model = UserQuestion()
    form = UserForm(request.POST or None, instance=model)
    ai_result = None
    if request.method == 'POST' and form.is_valid():
        question_instance = form.save()

        buyi= question_instance.buyi
        vazni= question_instance.vazni
        goal= question_instance.goal
        ai_result = ai_handler(buyi=buyi,vazni=vazni,goal=goal)

    ctx = {
        'form':form,
        'model':model,
        'ai_result':ai_result
    }
    return render(request,'ai_services/form.html',ctx)


