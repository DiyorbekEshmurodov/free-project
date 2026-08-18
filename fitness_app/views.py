from django.shortcuts import render, redirect, get_object_or_404
from .models import FitnessPlan
from .forms import FitnessPlanForm
from accounts.models import UserDetail
from django.contrib.auth.decorators import login_required


# Ro'yxatni ko'rish va hisobot olish
def plan_list(request):
    period = request.GET.get('period', 'daily')  # Standart kunlik
    plans = FitnessPlan.objects.filter(user=request.user.userdetail, period_type=period).order_by('target_date')

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
        return redirect('user_list')
    return render(request, 'fitness_app/form.html', {'form': form})


# Update
def plan_edit(request, pk):
    plan = get_object_or_404(FitnessPlan, pk=pk, user=request.user.userdetail)
    form = FitnessPlanForm(request.POST or None, instance=plan)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'fitness_app/form.html', {'form': form})


# Delete
def plan_delete(request, pk):
    plan = get_object_or_404(FitnessPlan, pk=pk, user=request.user.userdetail)
    plan.delete()
    return redirect('user_list')

def user_plan(request):
    has_profile = False

    if request.user.is_authenticated:
        # UserDetail modelida joriy foydalanuvchi bor-yo'qligini tekshiramiz
        has_profile = UserDetail.objects.filter(user=request.user).exists()

    context = {
        'has_profile': has_profile,
    }
    return render(request, 'index.html', context)

@login_required
def ai_report_view(request):
    profile = UserDetail.objects.filter(user=request.user).first()
    if not profile:
        return redirect('profile_setup')
    cards = [
        {'id': 'weight_loss', 'icon': '🔥', 'title': 'Vazn tashlash va yog\' eritish',
         'desc': 'Kaloriya defitsiti va yog\' yoqish rejasi.'},
        {'id': 'muscle_gain', 'icon': '💪', 'title': 'Mushak massasini oshirish',
         'desc': 'Gipertrofiya va oqsilga boy ratsion.'},
        {'id': 'stamina', 'icon': '⚡', 'title': 'Chidamlilik va Energiya',
         'desc': 'Kun davomida tetiklik va quvvatni oshirish.'},
        {'id': 'health_habits', 'icon': '🥗', 'title': 'Sog\'lom turmush tarzi',
         'desc': 'Kunlik to\'g\'ri odatlarni shakllantirish.'}
    ]

    selected_card = request.GET.get('card','weight_loss')
    selected_period = request.GET.get('period', 'daily')

    advice_data = generate_user_advice(profile,selected_card,selected_period)
    context = {
        'cards': cards,
        'selected_card': selected_card,
        'selected_period': selected_period,
        'advice_data': advice_data,
        'profile': profile
    }
    return render(request, 'fitness_app/reports.html', context)

def generate_user_advice(profile,card_id,period):
    buyi = getattr(profile,'buyi','Nomalum')
    vazni = getattr(profile,'vazni','Nomalum')
    maqsadi = getattr(profile,'maqsadi','Nomalum')

    period_names = {
        'daily': 'Kunlik',
        'weekly': 'Haftalik',
        'monthly': 'Oylik',
        'yearly': 'Yillik'
    }

    text = (
        f"Hurmatli **{profile.user.username}**, sizning ko'rsatkichlaringiz:\n"
        f"📏 **Bo'yingiz:** {buyi} cm | ⚖️ **Vazningiz:** {vazni} kg | 🎯 **Maqsadingiz:** {maqsadi}\n\n"
        f"Siz **{period_names.get(period, 'Kunlik')}** rejani tanladingiz.\n\n"
    )

    if period == 'daily':
        text += f"Bugungi kun uchun {vazni} kg vazningizga mos ravishda kamida {float(vazni) * 35 / 1000:.1f} litr suv ichishingiz hamda {float(vazni) * 1.6:.0f}g oqsil iste'mol qilishingiz tavsiya etiladi."
    elif period == 'weekly':
        text += f"Hafta davomida bo'yingiz ({buyi} cm) va vazningizga nisbatan 3 marotaba intensiv mashg'ulot bajarsangiz, taxminan 0.5 - 0.8 kg xavfsiz vazn yo'qotishingiz/oshirishingiz mumkin."
    elif period == 'monthly':
        text += f"1 oy davomida {maqsadi} maqsadingiz bo'yicha barqaror natijaga erishish uchun kunlik ratsioningizni belgilangan normada ushlab turing."
    else:
        text += f"Yillik strategiyangiz sizning uzoq muddatli salomatligingiz va {maqsadi} natijangizni saqlab qolishga qaratiladi."

    return text