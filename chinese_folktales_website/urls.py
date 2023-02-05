from django.urls import path
from chinese_folktales_website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name="login"),
    path('contact/', views.contact, name="contact"),
    path('stories/', views.stories, name="stories"),
    path('about/', views.about, name="about"),
    path('create_account/', views.create_account, name="create_account"),
    path('info_user/', views.info_user, name="info_user"),

]