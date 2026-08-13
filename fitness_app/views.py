from django.shortcuts import render, redirect, get_object_or_404
from .models import FitnessPlan
from .forms import FitnessPlanForm


# Ro'yxatni ko'rish va hisobot olish
def plan_list(request):
    period = request.GET.get('period', 'daily')  # Standart kunlik
    plans = FitnessPlan.objects.filter(user=request.user.userdetail, period_type=period).order_by('-target_date')

    ctx = {
        'plans': plans,
        'period': period
    }
    return render(request, "fitness_app/list.html", ctx)


# Create
def plan_create(request):
    form = FitnessPlanForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        plan = form.save(commit=False)
        plan.user = request.user.userdetail  # Logik bog'lanish
        plan.save()
        return redirect('plan_list')
    return render(request, 'fitness_app/form.html', {'form': form})


# Update
def plan_edit(request, pk):
    plan = get_object_or_404(FitnessPlan, pk=pk, user=request.user.userdetail)
    form = FitnessPlanForm(request.POST or None, instance=plan)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('plan_list')
    return render(request, 'fitness_app/form.html', {'form': form})


# Delete
def plan_delete(request, pk):
    plan = get_object_or_404(FitnessPlan, pk=pk, user=request.user.userdetail)
    plan.delete()
    return redirect('plan_list')

# from django.shortcuts import render , redirect
# from django.contrib.auth.decorators import login_required
# from .forms import *
# from .models import *
#
#
# # Hamma hisobotlardi oladi
# @login_required
# def hisobot_list(request):
#     hisobotlar = FitnessPlan.objects.filter(user_id=request.user.id)
#     ctx = {
#         'hisobotlar': hisobotlar
#     }
#     return render(request, "fitness_app/list.html", ctx)
#
# @login_required
# def hisobot_create(request):
#     model = FitnessPlan()
#     form = HisobotForm(request.POST or None, request.FILES or None, instance=model)
#
#     if request.method == 'POST' and form.is_valid():
#         plan = form.save(commit=False)
#         plan.user_id = request.user.id
#         plan.save()
#         return redirect('hisobot_list')
#
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'fitness_app/form.html', ctx)
#
# @login_required
# def hisobot_edit(request, pk):
#     model = FitnessPlan.objects.get(pk=pk, user_id=request.user.id)
#     form = HisobotForm(request.POST or None, request.FILES or None, instance=model)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('hisobot_list')
#
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'fitness_app/form.html', ctx)
#
# @login_required
# def hisobot_delete(request, pk):
#     model = FitnessPlan.objects.get(pk=pk)
#     model.delete()
#     return redirect('hisobot_list')
#
# @login_required
# def get_kunlik_list(request):
#     model = GetKunlik.objects.all()
#     ctx = {
#         'model': model,
#     }
#     return render(request, 'fitness_app/list.html', ctx)
#
# @login_required
# def get_kunlik_create(request):
#     model = GetKunlik()
#     form = GetKunlikForm(request.POST or None, instance=model)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('get_kunlik_list')
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'fitness_app/form.html', ctx)
#
# @login_required
# def get_kunlik_edit(request, pk):
#     model = GetKunlik.objects.get(pk=pk)
#     form = GetKunlikForm(request.POST or None, instance=model)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('get_kunlik_list')
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'fitness_app/form.html', ctx)
#
# @login_required
# def get_kunlik_delete(request,pk):
#     model = GetKunlik.objects.get(pk=pk)
#     model.delete()
#     return redirect('get_kunlik_list')
#
# @login_required
# def get_haftalik_list(request):
#     model = GetHaftalik.objects.all()
#     ctx = {
#         'model': model,
#     }
#     return render(request, 'fitness_app/list.html', ctx )
#
# @login_required
# def get_haftalik_create(request):
#     model = GetHaftalik()
#     form = GetHaftalikForm(request.POST or None, instance=model)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('get_haftalik_list')
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'fitness_app/form.html', ctx)
#
# @login_required
# def get_haftalik_edit(request, pk):
#     model = GetHaftalik.objects.get(pk=pk)
#     form = GetHaftalikForm(request.POST or None, instance=model)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('get_haftalik_list')
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'fitness_app/form.html', ctx)
#
# @login_required
# def get_haftalik_delete(request,pk):
#     model = GetHaftalik.objects.get(pk=pk)
#     model.delete()
#     return redirect('get_haftalik_list')
#
# @login_required
# def get_yillik_list(request):
#     model = GetYillik.objects.all()
#     ctx = {
#         'model': model,
#     }
#     return render(request, 'fitness_app/list.html', ctx)
#
# @login_required
# def get_yillik_create(request):
#     model = GetYillik()
#     form = GetYillikForm(request.POST or None, instance=model)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('get_yillik_list')
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'fitness_app/form.html', ctx)
#
# @login_required
# def get_yillik_edit(request, pk):
#     model = GetYillik.objects.get(pk=pk)
#     form = GetYillikForm(request.POST or None, instance=model)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('get_yillik_list')
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'fitness_app/form.html', ctx)
#
# @login_required
# def get_yillik_delete(request,pk):
#     model = GetYillik.objects.get(pk=pk)
#     model.delete()
#     return redirect('get_yillik_list')