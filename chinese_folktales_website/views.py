from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from .forms import CreateUser


def home(request):
    user = request.user
    if user is None:
        logout(request)
        messages.success(request, 'Etat : Non connecté')

    return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = User.objects.get(email=email).username
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Bienvenue sur Chinese Folktales ' + user.username + ' !')
            return redirect('home')
        else:
            messages.error(request, "Email et/ou mot de passe inconnus")
    return render(request, 'login.html')


def contact(request):
    return render(request, "contact.html")


def stories(request):
    return render(request, "stories.html")


def about(request):
    return render(request, "about.html")


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


def info_user(request):
    return render(request, "info_user.html")
