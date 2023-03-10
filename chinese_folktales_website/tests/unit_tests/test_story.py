from django.contrib.auth.models import User
from django.test import TestCase
from chinese_folktales_website.story_importer import StoryImporter
from chinese_folktales_website.models import Level, Story
from markdown import markdown

class TestStory(TestCase):

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

    def test_load_story(self):
        test_results = self.story_imported.load_story_list()
        expected_results = [
            {
                "title": "Je vois",
                "chinese_title": "我看到",
                "level": "Facile",
                "textfile": "je_vois.md",
                "audiofile": "https://github.com/nicoseng/P13_chinese_folktales/raw/0699a2879a5e86756c41b70cace05083a2f55e90/chinese_folktales_website/stories/audio/je_vois.mp3",
                "bg_image": "https://github.com/nicoseng/P13_chinese_folktales/raw/c818cf03190b4e7bedc03ce9e5f9552e3b2ca46a/chinese_folktales_website/static/images/je_vois.png",
                "audio_bg_image": "https://github.com/nicoseng/P13_chinese_folktales/raw/a39fa0f122829af2c3ed53e878eabaff472d6790/chinese_folktales_website/static/images/je_vois/audio_bg_image.png",
                "description": "Une petite exploration dans le jardin avec une souris comme guide ? C'est par ici que ça se passe ! "
            },
            {
                "title": "Mon équipe",
                "chinese_title": "我的隊伍",
                "level": "Facile",
                "textfile": "mon_equipe.md",
                "audiofile": "https://github.com/nicoseng/P13_chinese_folktales/raw/5017d80212878d6d19f353a9c2d95077f42fd284/chinese_folktales_website/stories/audio/mon_equipe.mp3",
                "bg_image": "https://github.com/nicoseng/P13_chinese_folktales/raw/c818cf03190b4e7bedc03ce9e5f9552e3b2ca46a/chinese_folktales_website/static/images/mon_equipe.png",
                "audio_bg_image": "",
                "description": "1, 2 ,3 ! Partez ! Que le meilleur gagne !"
            },
            {
                "title": "Grand et petit",
                "chinese_title": "大和小",
                "level": "Facile",
                "textfile": "grand_et_petit.md",
                "audiofile": "https://github.com/nicoseng/P13_chinese_folktales/raw/5017d80212878d6d19f353a9c2d95077f42fd284/chinese_folktales_website/stories/audio/grand_et_petit.mp3",
                "bg_image": "https://github.com/nicoseng/P13_chinese_folktales/raw/c818cf03190b4e7bedc03ce9e5f9552e3b2ca46a/chinese_folktales_website/static/images/grand_et_petit.png",
                "audio_bg_image": "",
                "description": "Grand ou petit ? Venez jeter un coup d'oeil !"
            },
            {
                "title": "Dans ma maison",
                "chinese_title": "我的家",
                "level": "Moyen",
                "textfile": "dans_ma_maison.md",
                "audiofile": "https://github.com/nicoseng/P13_chinese_folktales/raw/e85f3d5452e54499c3a35aa301279febb46d8b96/chinese_folktales_website/stories/audio/dans_ma_maison.mp3",
                "bg_image": "https://github.com/nicoseng/P13_chinese_folktales/raw/c818cf03190b4e7bedc03ce9e5f9552e3b2ca46a/chinese_folktales_website/static/images/dans_ma_maison.png",
                "audio_bg_image": "",
                "description": "Venez découvrir la maison de notre hôte. Et vous qu'y-a-t-il dans votre maison ?"
            },
            {
                "title": "J'aime",
                "chinese_title": "我喜歡",
                "level": "Moyen",
                "textfile": "j_aime.md",
                "audiofile": "https://github.com/nicoseng/P13_chinese_folktales/raw/5017d80212878d6d19f353a9c2d95077f42fd284/chinese_folktales_website/stories/audio/j_aime.mp3",
                "bg_image": "https://github.com/nicoseng/P13_chinese_folktales/raw/c818cf03190b4e7bedc03ce9e5f9552e3b2ca46a/chinese_folktales_website/static/images/j_aime.png",
                "audio_bg_image": "",
                "description": "J'aime ou j'aime pas ? Il y a certainement quelque chose que vous aimez."
            },
            {
                "title": "Mes cinq sens",
                "chinese_title": "我的五種感官",
                "level": "Moyen",
                "textfile": "mes_cinq_sens.md",
                "audiofile": "https://github.com/nicoseng/P13_chinese_folktales/raw/5017d80212878d6d19f353a9c2d95077f42fd284/chinese_folktales_website/stories/audio/mes_cinq_sens.mp3",
                "bg_image": "https://github.com/nicoseng/P13_chinese_folktales/raw/c818cf03190b4e7bedc03ce9e5f9552e3b2ca46a/chinese_folktales_website/static/images/mes_cinq_sens.png",
                "audio_bg_image": "",
                "description": "La vue, l'odorat, le goût, le toucher et l'ouïe, ça vous dit en mandarin ? Allez c'est parti !"
            },
            {
                "title": "Les grenouilles et leurs rois",
                "chinese_title": "青蛙和他們的國王",
                "level": "Difficile",
                "textfile": "les_grenouilles_et_leurs_rois.md",
                "audiofile": "https://github.com/nicoseng/P13_chinese_folktales/raw/5017d80212878d6d19f353a9c2d95077f42fd284/chinese_folktales_website/stories/audio/les_grenouilles_et_leurs_rois.mp3",
                "bg_image": "https://github.com/nicoseng/P13_chinese_folktales/raw/c818cf03190b4e7bedc03ce9e5f9552e3b2ca46a/chinese_folktales_website/static/images/les_grenouilles_et_leurs_rois.png",
                "audio_bg_image": "",
                "description": "Les grenouilles sont en quête de leurs rois et le font bien savoir. Arriveront-ils à accomplir cette mission ?"
            },
            {
                "title": "Deux petits lapins",
                "chinese_title": "兩隻小兔",
                "level": "Difficile",
                "textfile": "deux_petits_lapins.md",
                "audiofile": "https://github.com/nicoseng/P13_chinese_folktales/raw/0699a2879a5e86756c41b70cace05083a2f55e90/chinese_folktales_website/stories/audio/deux_petits_lapins.mp3",
                "bg_image": "https://github.com/nicoseng/P13_chinese_folktales/raw/c818cf03190b4e7bedc03ce9e5f9552e3b2ca46a/chinese_folktales_website/static/images/deux_petits_lapins.png",
                "audio_bg_image": "",
                "description": "Deux petits lapins s'amusent dans les champs et font une rencontre dans les bois. Que vont-ils leur arriver ?"
            },
            {
                "title": "Le lapin et la tortue",
                "chinese_title": "龜兔賽跑",
                "level": "Difficile",
                "textfile": "le_lapin_et_la_tortue.md",
                "audiofile": "https://github.com/nicoseng/P13_chinese_folktales/raw/e85f3d5452e54499c3a35aa301279febb46d8b96/chinese_folktales_website/stories/audio/le_lapin_et_la_tortue.mp3",
                "bg_image": "https://github.com/nicoseng/P13_chinese_folktales/raw/c818cf03190b4e7bedc03ce9e5f9552e3b2ca46a/chinese_folktales_website/static/images/le_lapin_et_la_tortue.png",
                "audio_bg_image": "",
                "description": "De quoi peuvent bien discuter un lapin et une tortue ?"
            }
        ]
        assert expected_results == test_results

    # def test_update_story_table(self):
    #     print(self.test_level_table.level_id)
    #     test_story_table = Story.objects.bulk_create([
    #         Story(
    #             story_id=1,
    #             level_id=Level.objects.get(level_id=self.test_level_table.level_id),
    #             title="Je vois",
    #             chinese_title="我看到",
    #             textfile="je_vois.md",
    #             audiofile="https://github.com/nicoseng/P13_chinese_folktales/raw/0699a2879a5e86756c41b70cace05083a2f55e90/chinese_folktales_website/stories/audio/je_vois.mp3",
    #             bg_image="https://github.com/nicoseng/P13_chinese_folktales/raw/c818cf03190b4e7bedc03ce9e5f9552e3b2ca46a/chinese_folktales_website/static/images/je_vois.png",
    #             audio_bg_image="https://github.com/nicoseng/P13_chinese_folktales/raw/a39fa0f122829af2c3ed53e878eabaff472d6790/chinese_folktales_website/static/images/je_vois/audio_bg_image.png",
    #             description="Une petite exploration dans le jardin avec une souris comme guide ? C'est par ici que ça se passe ! "
    #         ),
    #         Story(
    #             story_id=2,
    #             level_id=Level.objects.get(level_id=self.test_level_table.level_id),
    #             title="Grand et petit",
    #             chinese_title="大和小",
    #             textfile="grand_et_petit.md",
    #             audiofile="https://github.com/nicoseng/P13_chinese_folktales/raw/5017d80212878d6d19f353a9c2d95077f42fd284/chinese_folktales_website/stories/audio/grand_et_petit.mp3",
    #             bg_image="https://github.com/nicoseng/P13_chinese_folktales/raw/c818cf03190b4e7bedc03ce9e5f9552e3b2ca46a/chinese_folktales_website/static/images/grand_et_petit.png",
    #             audio_bg_image="",
    #             description="Grand ou petit ? Venez jeter un coup d'oeil !"
    #         ),
    #     ])
    #
    #     test_results = self.story_imported.update_story_table(self.test_story_list, self.test_level_table, test_story_table)
    #     print(test_results)
    #     print(type(test_results))
    #     expected_results = Story.objects.values()

    def test_inject_story_in_database(self):

        test_results = self.story_imported.inject_story_in_database(
            self.test_story_list,
            self.test_level_table,
            self.test_story_table
        )
        expected_results = Story.objects.all()
        assert len(test_results) == len(expected_results)

    def test_open_textfile(self):
        textfile_basepath = '/Users/nicolassengmany/Desktop/OCR/Python/Projets/P13/chinese_folktales/chinese_folktales_website/stories/texts/'
        textfile_name = 'grand_et_petit.md'
        story_file = textfile_basepath + textfile_name
        with open(story_file, 'r') as story_content:
            content = story_content.read()
        expected_results = markdown(content)

        test_results = self.story_imported.open_textfile(textfile_name)
        assert test_results == expected_results
