from django.shortcuts import render, redirect
from .models import CustomUser, CustomUserManager
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout as auth_logout
from django.core.mail.message import EmailMessage
from .forms import ProfileImageForm, ChangeNicknameForm
from django.contrib.auth.decorators import login_required
@csrf_protect

#회원가입
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        nickname = request.POST['nickname']
        password = request.POST['password']
        email = request.POST['email']

        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            email=email,
            nickname=nickname,
        )
        login(request, user=user)
        return redirect('accounts:login_view')

    return render(request, 'signup.html')

#로그인
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('accounts:mypage') # 로그인 성공 시 이동할 URL 연결할 곳
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

#로그아웃
def logout(request):
    auth_logout(request)
    return redirect('login_view')

def home(request):
    return render(request, 'home.html')
    

#마이페이지
def mypage(request):
    if request.method == "POST":
        '''
        new_nickname = request.POST.get('new_nickname','')
        if new_nickname:
            request.user.nickname = new_nickname
            request.user.save()'''
    image_form = ProfileImageForm(instance=request.user)
    if request.method == "POST":
        image_form = ProfileImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()

    return render(request, 'mypage.html', {
        #'user':user,
        'image_form':image_form
    })

#닉네임 변경
def change_nickname(request):
    if request.method == 'POST':
        form = ChangeNicknameForm(request.POST)
        if form.is_valid():
            new_nickname = form.cleaned_data['new_nickname']
            request.user.nickname = new_nickname
            request.user.save()
            return redirect('accounts:mypage')
    else:
        form = ChangeNicknameForm()
    return render(request, 'nickname.html',{'form':form})
#메일보내기