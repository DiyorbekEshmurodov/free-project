from django.shortcuts import render , redirect
from django.http import JsonResponse
from .models import FitnessPlan
from forms import HisobotForm


def hisobot_list(request):
    hisobotlar = FitnessPlan.objects.filter(user_id=request.user.id)
    ctx = {
        'hisobotlar': hisobotlar
    }
    return render(request, "fitness/list.html", ctx)

def hisobot_create(request):
    model = FitnessPlan()
    form = HisobotForm(request.POST or None, request.FILES or None, instance=model)

    if request.method == 'POST' and form.is_valid():
        plan = form.save(commit=False)
        plan.user_id = request.user.id
        plan.save()
        return redirect('hisobot_list')

    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'fitness/form.html', ctx)

def hisobot_edit(request, pk):
    model = FitnessPlan.objects.get(pk=pk, user_id=request.user.id)
    form = HisobotForm(request.POST or None, request.FILES or None, instance=model)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('hisobot_list')

    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'fitness/form.html', ctx)

def hisobot_delete(request, pk):
    model = FitnessPlan.objects.get(pk=pk)
    model.delete()
    return redirect('hisobot_list')