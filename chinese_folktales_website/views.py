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
from .forms import CreateUser, UpdateUserForm, ChangePasswordForm
from .level_importer import LevelImporter
from .story_importer import StoryImporter
from .favorite import StoryInFavorite
from .delete_story import StoryEliminator
from .models import Story, Favorite


def home(request):
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
    context = {"story_table": story_table}
    return render(request, "stories.html", context)


def story_detail(request, story_id):
    story = Story.objects.get(story_id=story_id)
    story_imported = StoryImporter()
    textfile = story_imported.open_textfile(story.textfile)
    context = {"story": story,
               "textfile": textfile,
               }
    return render(request, "story_detail.html", context)


def about(request):
    return render(request, "about.html")


@login_required(login_url="login")
def add_favorite(request, story_id):
    # We fetch the id of the user
    current_user = request.user
    user_id = current_user.id
    story_id = Story.objects.get(story_id=story_id).story_id

    if request.method == "POST":
        favorite_database = StoryInFavorite()
        favorite_database = favorite_database.inject_story_in_favorite(story_id, user_id)
        context = {"favorite_database": favorite_database}
        return render(request, "display_favorite.html", context)


@login_required(login_url="login")
def display_favorite(request):
    current_user = request.user
    user_id = current_user.id
    # user_id = User.objects.get(id=user_id)
    favorite_database = StoryInFavorite()
    favorite_database = favorite_database.retrieve_favorite_database(user_id)

    context = {"favorite_database": favorite_database}
    return render(request, 'display_favorite.html', context)


@login_required(login_url="login")
def delete_story(request, story_id):
    story_id = Story.objects.get(story_id=story_id)
    if request.method == "POST":
        story_deleted = StoryEliminator()
        favorite_database = story_deleted.delete_story(story_id)
        context = {"favorite_database": favorite_database}
        return render(request, 'display_favorite.html', context)


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
    user = request.user
    change_password_form = ChangePasswordForm(user, request.POST)
    if request.method == 'POST':
        if change_password_form.is_valid():
            change_password_form.save()
            messages.success(request, "Mot de passe bien modifié !")
            return redirect('login')
        else:
            messages.error(request,
                           mark_safe("Erreur : Mot de passe différents !<br/>Veuillez recommencer votre saisie"))
            change_password_form = ChangePasswordForm(user, request.POST)

    context = {'change_password_form': change_password_form}
    return render(request, 'change_password.html', context)


def update_user(request):
    actual_user_data = User.objects.get(username=request.user)
    if request.method == "POST":
        update_user_form = UpdateUserForm(request.POST, instance=actual_user_data)
        new_username = update_user_form["new_username"].value()
        new_email = update_user_form["new_email"].value()
        if update_user_form.is_valid():
            update_user_form.save()
            new_user_data = update_user_form.update_user(
                actual_user_data,
                new_username,
                new_email,
                actual_user_data.password
            )
            messages.success(request, 'Profil bien mis à jour pour ' + new_user_data.username + ' !')
            return redirect('login')
    else:
        update_user_form = UpdateUserForm(request.POST)

    context = {'update_user_form': update_user_form}
    return render(request, 'update_user.html', context)


def submit_mail(request):
    current_user = request.user
    if request.method == "POST":
        message = request.POST["message"]
        send_mail(
            'Message',
            message,
            current_user.email,
            ['sengmanynicolas21@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, "Message bien envoyé ! ")

    return render(request, 'contact.html')
