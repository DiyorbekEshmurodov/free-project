from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import FitnessPlan
from .forms import FitnessPlanForm
from accounts.models import UserDetail


# ----------------------------------------------------
# 1. FITNESS PLAN CRUD FUNKSIYALARI (ESKI FUNKSIYALAR)
# ----------------------------------------------------

@login_required
def plan_list(request):
    profile = UserDetail.objects.filter(user=request.user).first()
    if not profile:
        return redirect('profile_setup')
    period = request.GET.get('period', 'daily')
    plans = FitnessPlan.objects.filter(user=profile, period_type=period).order_by('target_date')

    ctx = {
        'plans': plans,
        'period': period
    }
    return render(request, "fitness_app/list.html", ctx)


@login_required
def plan_create(request):
    profile = UserDetail.objects.filter(user=request.user).first()
    if not profile:
        return redirect('profile_setup')
    form = FitnessPlanForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        plan = form.save(commit=False)
        plan.user = profile
        plan.save()
        return redirect('user_list')
    return render(request, 'fitness_app/form.html', {'form': form})


@login_required
def plan_edit(request, pk):
    profile = UserDetail.objects.filter(user=request.user).first()
    if not profile :
        return redirect('profile_setup')
    plan = get_object_or_404(FitnessPlan, pk=pk, user=profile)
    form = FitnessPlanForm(request.POST or None, instance=plan)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'fitness_app/form.html', {'form': form})


@login_required
def plan_delete(request, pk):
    profile  = UserDetail.objects.filter(user=request.user).first()
    if not profile:
        return redirect('profile_setup')
    plan = get_object_or_404(FitnessPlan, pk=pk, user=profile)
    plan.delete()
    return redirect('user_list')


def user_plan(request):
    has_profile = False
    if request.user.is_authenticated:
        has_profile = UserDetail.objects.filter(user=request.user).exists()

    context = {
        'has_profile': has_profile,
    }
    return render(request, 'index.html', context)


# ----------------------------------------------------
# 2. AI REPORT GENERIC VIEW & TAVSIYA GENERATORI
# ----------------------------------------------------

class AIReportView(LoginRequiredMixin, TemplateView):
    template_name = 'fitness_app/ai_page.html'

    def dispatch(self, request, *args, **kwargs):
        # Profil to'ldirilmagan bo'lsa, xavfsiz yo'naltirish
        if request.user.is_authenticated and not UserDetail.objects.filter(user=request.user).exists():
            return redirect('profile_setup')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Foydalanuvchi profilini xavfsiz olish
        profile = UserDetail.objects.filter(user=self.request.user).first()

        cards = [
            {'id': 'weight_loss', 'icon': '🔥', 'title': "Vazn tashlash va yog' eritish", 'desc': "Kaloriya defitsiti va yog' yoqish rejasi."},
            {'id': 'muscle_gain', 'icon': '💪', 'title': "Mushak massasini oshirish", 'desc': "Gipertrofiya va oqsilga boy ratsion."},
            {'id': 'stamina', 'icon': '⚡', 'title': "Chidamlilik va Energiya", 'desc': "Kun davomida tetiklik va quvvatni oshirish."},
            {'id': 'health_habits', 'icon': '🥗', 'title': "Sog'lom turmush tarzi", 'desc': "Kunlik to'g'ri odatlarni shakllantirish."}
        ]

        selected_card = self.request.GET.get('card', 'weight_loss')
        selected_period = self.request.GET.get('period', 'daily')

        # Foydalanuvchining FitnessPlan jadvalidagi ma'lumotlarini olish
        user_plans = FitnessPlan.objects.filter(user=profile, period_type=selected_period) if profile else []

        # Dinamik AI maslahatini shakllantirish
        advice_data = self.generate_user_advice(profile, selected_card, selected_period, user_plans)

        context.update({
            'cards': cards,
            'selected_card': selected_card,
            'selected_period': selected_period,
            'advice_data': advice_data,
            'profile': profile,
            'user_plans': user_plans,
        })
        return context

    def generate_user_advice(self, profile, card_id, period, user_plans):
        if not profile:
            return "Profil ma'lumotlari topilmadi."

        buyi = getattr(profile, 'buyi', 'Noma\'lum')
        vazni = getattr(profile, 'vazni', 'Noma\'lum')
        maqsadi = getattr(profile, 'maqsadi', 'Noma\'lum')

        period_names = {
            'daily': 'Kunlik',
            'weekly': 'Haftalik',
            'monthly': 'Oylik',
            'yearly': 'Yillik'
        }

        card_names = {
            'weight_loss': "Vazn tashlash va yog' eritish",
            'muscle_gain': "Mushak massasini oshirish",
            'stamina': "Chidamlilik va Energiya",
            'health_habits': "Sog'lom turmush tarzi"
        }

        text = (
            f"Hurmatli **{profile.user.username}**, sizning ko'rsatkichlaringiz:\n"
            f"📏 **Bo'yingiz:** {buyi} cm | ⚖️ **Vazningiz:** {vazni} kg | 🎯 **Maqsadingiz:** {maqsadi}\n\n"
            f"📌 Tanlangan yo'nalish: **{card_names.get(card_id, 'Umumiy')}** ({period_names.get(period, 'Kunlik')} reja)\n\n"
        )

        # Karta turi va tanlangan vaqt bo'yicha dinamik mantiq
        if card_id == 'weight_loss':
            return {
                'nutrition': f"Kunlik ratsioningizdan 300-500 kcal kamaytirib, kamida {float(vazni) * 35 / 1000:.1f}L suv ichishingiz tavsiya etiladi.",
                'workout': "Haftasiga 3-4 marotaba kam intensivlikdagi kardio va yengil kuch mashqlarini bajaring.",
                'ai_recommendation': f"Vazningiz {vazni} kg bo'lgani uchun yog' yoqish jarayonini tezlashtirish maqsadida oqsil balansini ushlab turing."
            }
        elif card_id == 'muscle_gain':
            return {
                'nutrition': f"Kunlik oqsil miqdorini {float(vazni) * 1.8:.0f}g ga yetkazing va murakkab uglevodlarni ko'paytiring.",
                'workout': "Mushak gipertrofiyasi uchun 8-12 takrorlanishdan iborat og'ir vaznli mashqlarga e'tibor bering.",
                'ai_recommendation': "Har bir mushak guruhiga mashqdan keyin kamida 48 soat tiklanish uchun vaqt bering."
            }
        elif card_id == 'stamina':
            return {
                'nutrition': "Energiyani barqaror ushlash uchun kunlik ovqatlanishda vitamin va minerallarga boy mahsulotlarni tanlang.",
                'workout': "Interval yugurish, arqon sakrash va funksional mashqlarni haftasiga 3 marotaba bajaring.",
                'ai_recommendation': "Nafas olish texnikasi va uyqu rejimiga (7-8 soat) qat'iy amal qiling."
            }
        else:  # health_habits
            return {
                'nutrition': "Kunlik ratsionda meva, sabzavotlar va yetarli miqdorda toza suv bo'lishini ta'minlang.",
                'workout': "Har kuni kamida 8,000 - 10,000 qadam piyoda yurishni odat qiling.",
                'ai_recommendation': "Sog'lom turmush tarzi intizomga asoslanadi. Har kuni kichik qadamlar bilan maqsad sari bering."
            }

        # Foydalanuvchining shaxsiy rejalari (FitnessPlan) haqida axborot
        if user_plans:
            text += f"\n\n📋 **Siz to'ldirgan rejalaringiz:** Ushbu davr uchun {user_plans.count()} ta rejangiz bazada mavjud va ular AI hisoboti shakllantirilishida inobatga olindi."

        return text