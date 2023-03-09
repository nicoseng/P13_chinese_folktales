from django.contrib.auth.models import User
from django.test import TestCase
from chinese_folktales_website.story_importer import StoryImporter
from chinese_folktales_website.models import Level, Story


class TestFavorite(TestCase):

    def setUp(self):
        self.story_imported = StoryImporter()
        self.user = User.objects.create(id=1, username="Arnaud")
        self.test_story_list = [
            {
              "title": "Je vois",
              "chinese_title": "我看到",
              "level": "Facile",
              "textfile": "je_vois.md",
              "audiofile": "https://github.com/nicoseng/P13_chinese_folktales/raw/0699a2879a5e86756c41b70cace05083a2f55e90/chinese_folktales_website/stories/audio/je_vois.mp3",
              "bg_image": "https://github.com/nicoseng/P13_chinese_folktales/raw/c818cf03190b4e7bedc03ce9e5f9552e3b2ca46a/chinese_folktales_website/static/images/je_vois.png",
              "audio_bg_image": "https://github.com/nicoseng/P13_chinese_folktales/raw/a39fa0f122829af2c3ed53e878eabaff472d6790/chinese_folktales_website/static/images/je_vois/audio_bg_image.png",
              "description": "Une petite exploration dans le jardin avec une souris comme guide ? C'est par ici que ça se passe ! "
            }
        ]
        self.test_level_table = Level.objects.create(
            level_id=1,
            name="Facile",
        )
        self.test_story_table = Story.objects.all()

    def test_inject_story_in_database(self):
        test_results = self.story_imported.inject_story_in_database(self.test_story_list, self.test_level, self.test_story_table)
