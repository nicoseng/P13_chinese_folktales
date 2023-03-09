from django.contrib.auth.models import User
from django.test import TestCase
from chinese_folktales_website.models import Level, Story, Favorite


class TestModels(TestCase):

    def setUp(self):

        self.user = User.objects.create(username="Arnaud")
        self.test_level = Level.objects.create(
            level_id=1,
            name="Facile",
        )

        self.test_story = Story.objects.create(
            level_id=Level(self.test_level.level_id),
            story_id=1,
            title="je_vois",
            chinese_title="我看到",
            textfile="je_vois.md",
            audiofile="https://github.com/nicoseng/P13_chinese_folktales/raw/0699a2879a5e86756c41b70cace05083a2f55e90/chinese_folktales_website/stories/audio/je_vois.mp3",
            bg_image="https://github.com/nicoseng/P13_chinese_folktales/raw/c818cf03190b4e7bedc03ce9e5f9552e3b2ca46a/chinese_folktales_website/static/images/je_vois.png",
            audio_bg_image="https://github.com/nicoseng/P13_chinese_folktales/raw/a39fa0f122829af2c3ed53e878eabaff472d6790/chinese_folktales_website/static/images/je_vois/audio_bg_image.png",
            description="Une petite exploration dans le jardin avec une souris comme guide ? C'est par ici que ça se passe ! "
        )

        self.test_favorite = Favorite.objects.create(
            user_id=self.user,
            story_id=Story(self.test_story.story_id),
        )

    def test_level_inserted_in_database(self):
        self.assertEqual(self.test_level.name, "Facile")

    def test_story_inserted_in_database(self):
        self.assertEqual(self.test_story.title, "je_vois")

    def test_favorite_inserted_in_database(self):
        self.assertEqual(self.test_favorite.story_id, Story(self.test_story.story_id))
