# import pytest
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.test import TestCase, Client
# from django.urls import reverse
# from django.utils.safestring import mark_safe
# from django.contrib.messages import get_messages
#
# from chinese_folktales_website.forms import CreateUser, ChangePasswordForm, UpdateUserForm
# from chinese_folktales_website.models import Level, Story, Favorite
# from chinese_folktales_website.level_importer import LevelImporter
# from chinese_folktales_website.favorite import StoryInFavorite
#
#
# class TestViews(TestCase):
#
#     @pytest.mark.django_db
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username="Louis",
#             email="louis@gmail.com",
#             password="lunaires"
#         )
#
#     def test_not_authenticated_user(self):
#         url = reverse('home')
#         response = self.client.get(url)
#         self.assertTemplateNotUsed(response, 'create_account.html')
#         self.assertEqual(response.status_code, 200)
