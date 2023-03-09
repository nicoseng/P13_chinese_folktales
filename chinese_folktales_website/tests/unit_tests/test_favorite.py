from django.contrib.auth.models import User
from django.test import TestCase

from chinese_folktales_website.favorite import StoryInFavorite
from chinese_folktales_website.models import Level, Story, Favorite


class TestFavorite(TestCase):

    def setUp(self):
        self.favorite_imported = StoryInFavorite()
        self.user = User.objects.create(id=1, username="Arnaud")
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

        # self.test_favorite = Favorite.objects.create(
        #     user_id=self.user,
        #     story_id=Story(self.test_story.story_id)
        # )
    def test_inject_story_in_favorite(self):

        test_results = self.favorite_imported.inject_story_in_favorite(self.test_story.story_id, self.user.id)
        expected_results = Favorite.objects.all()
        assert len(test_results) == len(expected_results)

    def test_retrieve_favorite_database(self):
        test_favorite = Favorite.objects.create(
            user_id=User(self.user.id),
            story_id=Story(self.test_story.story_id)
        )
        test_results = self.favorite_imported.retrieve_favorite_database(test_favorite.user_id)
        expected_results = Favorite.objects.all()
        assert len(test_results) == len(expected_results)

