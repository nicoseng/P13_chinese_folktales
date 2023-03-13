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
    path('display_favorite/', views.display_favorite, name="display_favorite"),
    path('delete_story/<int:story_id>', views.delete_story, name='delete_story'),
    path('stories/<int:story_id>/add_favorite/', views.add_favorite, name='add_favorite'),
    path('create_account/', views.create_account, name="create_account"),
    path('info_user/', views.info_user, name="info_user"),
    path('change_password/', views.change_password, name="change_password"),
    path('update_user/', views.update_user, name="update_user"),
    path('admin/', admin.site.urls),
]
