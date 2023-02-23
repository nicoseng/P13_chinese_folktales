from django.contrib import admin
from django.urls import path
from chinese_folktales_website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name="login"),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('contact/', views.contact, name="contact"),
    path('contact/submit_mail', views.submit_mail, name="submit_mail"),
    path('stories/', views.stories, name="stories"),
    path('stories/<int:story_id>/', views.story_detail, name="story_detail"),
    path('about/', views.about, name="about"),
    path('favorite/', views.favorite, name="favorite"),
    path('create_account/', views.create_account, name="create_account"),
    path('info_user/', views.info_user, name="info_user"),
    path('change_password/', views.change_password, name="change_password"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('admin/', admin.site.urls),
]
