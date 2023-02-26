from requests import get

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
from .forms import CreateUser
from .level_importer import LevelImporter
from .story_importer import StoryImporter
from .models import Story


def home(request):
    user = request.user
    if user is None:
        logout(request)
    return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = User.objects.get(email=email).username
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Email et/ou mot de passe inconnus")
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return render(request, 'home.html')


@login_required(login_url="login")
def contact(request):
    return render(request, "contact.html")


def stories(request):
    story_table = Story.objects.all()
    print(story_table)
    context = {"story_table": story_table}
    return render(request, "stories.html", context)


def story_detail(request, story_id):
    story_id = Story.objects.get(story_id=story_id)
    context = {"story_id": story_id}
    return render(request, "story_detail.html", context)


def open_audiofile(request, story_id):
    story_id = Story.objects.get(story_id=story_id)
    context = {"story_id": story_id}
    return render(request, "story_detail.html", context)


def about(request):
    return render(request, "about.html")


def user_directory_path(request, story_id):
    story_id = Story.objects.get(story_id=story_id)
    context = {"story_id": story_id}
    return render(request, "story_detail.html", context)

@login_required(login_url="login")
def favorite(request):
    return render(request, "favorite.html")


def create_account(request):
    create_account_form = CreateUser()
    if request.method == "POST":
        create_account_form = CreateUser(request.POST)
        if create_account_form.is_valid():
            create_account_form.save()
            username = create_account_form.cleaned_data.get('username')
            messages.success(request, 'Compte crée avec succès pour ' + username + ' !')
            return redirect('login')
    context = {'create_account_form': create_account_form}
    return render(request, 'create_account.html', context)


@login_required(login_url="login")
def info_user(request):
    return render(request, "info_user.html")


def change_password(request):
    return render(request, "change_password.html")


def edit_profile(request):
    return render(request, "edit_profile.html")


def submit_mail(request):
    current_user = request.user
    print(current_user.email)
    if request.method == "POST":
        message = request.POST["message"]
        print(message)
        send_mail(
            'Message',
            message,
            current_user.email,
            ['sengmanynicolas21@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, "Message bien envoyé ! ")

    return render(request, 'contact.html')
