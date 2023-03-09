import pytest
from django.contrib import messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.messages import get_messages
from django.core import mail
from django.core.mail import send_mail
from chinese_folktales_website.forms import CreateUser, ChangePasswordForm, UpdateUserForm
from chinese_folktales_website.models import Level, Story, Favorite
from chinese_folktales_website.level_importer import LevelImporter
from chinese_folktales_website.favorite import StoryInFavorite


class TestViews(TestCase):

    @pytest.mark.django_db
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="Louis",
            email="louis@gmail.com",
            password="lunaires"
        )

    def test_not_authenticated_user(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, 'create_account.html')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user(self):
        self.client.login(username="Louis", password="lunaires")
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.client.logout()

    def test_home_view(self):
        self.client.get('home/')
        path = reverse('home')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_stories_view(self):
        self.client.get('stories/')
        path = reverse('stories')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_display_favorite_view(self):
        self.client.get('display_favorite/')
        path = reverse('display_favorite')
        response = self.client.get(path)
        assert response.status_code == 302

    def test_delete_story_view(self):
        self.client.get('delete_story/')
        path = reverse('delete_story')
        response = self.client.get(path)
        assert response.status_code == 302
    
    def test_contact_view(self):
        self.client.get('contact/')
        path = reverse('contact')
        response = self.client.get(path)
        assert response.status_code == 302
    
    def test_about_view(self):
        self.client.get('about/')
        path = reverse('about')
        response = self.client.get(path)
        assert response.status_code == 200

    # def test_stories_view(self):
    #     self.client.get('stories/')
    #     path = reverse('story_detail')
    #     response = self.client.get(path)
    #     assert response.status_code == 200

    def test_create_account_view(self):
        form = CreateUser(
            {"username": "Jeanne",
             "email": "abc@gmail.com",
             "password1": "lunaires",
             "password2": "lunaires"
             }
        )
        assert form.is_valid()

        if form.is_valid():
            form.save()
            assert form.cleaned_data.get('username') == "Jeanne"
            user = form.save()
            self.assertEqual(user.username, "Jeanne")
            self.client.get(reverse('create_account'), follow=True)
        else:
            self.fail("User not valid")

        credentials = {"username": "Lucien", "email": "abc@gmail.com"}
        User.objects.create_user(**credentials)

        # send create_account data
        self.client.post('/create_account/', credentials, follow=True)
        path = reverse('create_account')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_login_user_view(self):
        credentials = {"username": "jeanne", "password": "lunaires", "email": "abc@gmail.com"}
        User.objects.create_user(**credentials)

        # send login data
        response = self.client.post('/login/', credentials, follow=True)
        # should be logged in now
        #self.assertTrue(response.context['user'].is_active)

        path = reverse('login')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_logout_user_view(self):
        path = reverse('logout_user')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_info_user_view(self):

        self.client.login(username="Louis", password="lunaires")
        response = self.client.get(reverse('info_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'info_user.html')

    def test_change_password_view(self):
        self.client.login(username="Louis", password="lunaires")
        path = reverse('change_password')
        response = self.client.get(path)
        assert response.status_code == 200

        new_pwd_data = {
            "new_password1": "solaires",
            "new_password2": "solaires"
        }
        rec = self.client.post('/change_password', new_pwd_data, follow=True)
        assert rec.status_code == 200

    def test_change_password_no_valid_view(self):
        self.client.login(username="Louis", password="lunaires")
        path = reverse('change_password')
        response = self.client.get(path)
        assert response.status_code == 200

        new_pwd_data = {
            "new_password1": "solaires",
            "new_password2": "molaires"
        }
        self.client.post('change_password', new_pwd_data, follow=True)

    def test_update_user_view(self):

        # To simule a connection
        self.client.login(username="Louis", password="lunaires")
        path = reverse('update_user')
        response = self.client.get(path)
        assert response.status_code == 200
        new_user_data = {
            "new_username": "test",
            "new_email": "test@gmail.com"
        }
        rec = self.client.post('/update_user', new_user_data, follow=True)
        assert rec.status_code == 200

    def test_submit_mail_view(self):
        self.client.login(
            username="Louis", password="lunaires")
        path = reverse('submit_mail')
        message = {
            "message": "test"
        }
        response = self.client.post(path, message)
        assert response.status_code == 200

        mail.send_mail(
            'Message',
            'test',
            'ccf1860bcba7f3',
            ['sengmanynicolas21@gmail.com']
        )

        # Now you can test delivery and email contents
        assert len(mail.outbox) == 2, "Inbox is not empty"
        assert mail.outbox[0].subject == 'Message'
        assert mail.outbox[0].body == 'test'
        assert mail.outbox[0].from_email == 'louis@gmail.com'
        assert mail.outbox[0].to == ['sengmanynicolas21@gmail.com']
