from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from django.db.models import Q

@login_required
def dashboard_view(request):
    # UserDetail ni 'user' va 'telegram_user' ustunlari bo'yicha izlaymiz
    profil = UserDetail.objects.filter(
        Q(user=request.user) | Q(telegram_user=request.user)
    ).first()

    # Profil to'liq to'ldirilganligini tekshiramiz
    has_profile = False
    if profil and profil.buyi and profil.vazni and profil.jinsi:
        has_profile = True

    context = {
        'profil': profil,
        'has_profile': has_profile,
    }
    # Agar HTML faylingiz nomi index.html bo'lsa, shuni ko'rsatasiz
    return render(request, 'index.html', context)

def login_required_decorator(func):
    return login_required(func,login_url='login_page')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('home')

@login_required_decorator
def profile_setup(request):
    profile, created = UserDetail.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserDetailForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            request.user.first_name = request.POST.get('first_name', request.user.first_name)
            request.user.last_name = request.POST.get('last_name', request.user.last_name)
            request.user.save()
            messages.success(request, "Ma'lumotlaringiz muvaffaqiyatli saqlandi!")
            return redirect('index')
    else:
        form = UserDetailForm(instance=profile)

    return render(request, 'accounts/profile.html', {'form': form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        action_type = request.POST.get('action_type')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone')

        if action_type == 'login':
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else :
                return render(request,'accounts/login.html',{'error':'Username yoki parol xato kiritilgan\nQaytadan kiriting 😁 '})

        elif action_type == 'register':
            confirm_password = request.POST.get('confirm_password')
            if password != confirm_password:
                messages.error(request,'Parollar bir hil emas')
            elif User.objects.filter(username=username).exists():
                    messages.error(request,'Bunday Foydalanuvchi alloqachon mavjud!')
            else:
                new_user = User.objects.create_user(username=username,password=password)
                new_user.save()
                login(request, new_user)
                return redirect('index')

        elif action_type == 'reset':
            confirm_password = request.POST.get('confirm_password')
            try :
                user = User.objects.get(username=username)
                if password == confirm_password:
                    user.set_password(password)
                    user.save()
                    login(request, user)
                    return redirect('index')
                else :
                    messages.error(request,"Yangi parollar mos kelmadi!")
            except User.DoesNotExist:
                    messages.error(request, 'Bunday foydalanuvchi topilmadi!')

    return render(request,'accounts/login.html')



def main_account(request):
    return render(request,'home.html')

def index_page(request):
    return render(request, 'index.html')

