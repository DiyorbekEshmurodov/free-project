from django.shortcuts import render, redirect, get_object_or_404
from .models import FitnessPlan
from .forms import FitnessPlanForm
from accounts.models import UserDetail


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

def user_plan(request):
    has_profile = False

    if request.user.is_authenticated:
        # UserDetail modelida joriy foydalanuvchi bor-yo'qligini tekshiramiz
        has_profile = UserDetail.objects.filter(user=request.user).exists()

    # Terminalda aniq ko'rish uchun formatlab print qilamiz
    print(f"=== HAS PROFILE QIYMATI: {has_profile} | USER: {request.user} ===")

    context = {
        'has_profile': has_profile,
    }
    return render(request, 'index.html', context)