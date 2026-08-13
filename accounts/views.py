from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def login_required_decorator(func):
    return login_required(func,login_url='login_page')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')


        if password != confirm_password :
            return render(request,'accounts/login.html',{'error':'Parol bir xil emas\nQaytadan kiriting 😁 '})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else :
            return render(request,'accounts/login.html',{'error':'Username yoki parol xato kiritilgan\nQaytadan kiriting 😁 '})

    return render (request,'accounts/login.html')

def main_account(request):
    return render(request,'home.html')

def index_page(request):
    return render(request, 'index.html')

