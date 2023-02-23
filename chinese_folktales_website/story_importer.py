from chinese_folktales_website.models import Story, Level
from pathlib import Path
from bs4 import BeautifulSoup
from slugify import slugify
import markdown
import os
import requests

class StoryImporter:
    """
    Import Stories and insert them in the story data table.
    """

    @staticmethod
    def load_story_list():
        #
        # stories_folder_path = "/Users/nicolassengmany/Desktop/OCR/Python/Projets/P13/chinese_folktales/chinese_folktales_website/stories/"
        # stories_content_list = os.listdir(stories_folder_path)
        # print(stories_content_list)
        #
        # for item in stories_content_list:
        #     if item != '.DS_Store':
        #         story_file_path = stories_folder_path + "{}".format(item)
        #         print(story_file_path)
        #         with open(story_file_path) as story_file:
        #             # read the file
        #             read_content = story_file.read()
        #             print(read_content)
        #
        #             story_html = markdown.markdown(read_content)
        #             print(story_html)
        #
        #             s = BeautifulSoup(story_html, 'html.parser')
        #             print("Voici votre résulat:", s)

        res = requests.get("https://github.com/nicoseng/P13_chinese_folktales/blob/main/chinese_folktales_website/static/js/story_mini_api.json")
        print(res)

        # Récupérer à partir de github (extraire les données ici)
        story_list = [
            {"title": "Grand et petit", "level": "Débutant", "bg_image": ""},
            {"title": "Le singe cupide", "level": "Débutant+", "bg_image": "grand_et_petit.png"},
            {"title": "Je vois", "level": "Débutant+", "bg_image": "grand_et_petit.png"},
            {"title": "H4", "level": "Intermédiaire", "bg_image": "grand_et_petit.png"},
            {"title": "H5", "level": "Intermédiaire+", "bg_image": "grand_et_petit.png"},
            {"title": "Deux petits lapins", "level": "Avancé", "bg_image": "grand_et_petit.png"},
            {"title": "H6", "level": "Avancé+", "bg_image": "grand_et_petit.png"},
            {"title": "H7", "level": "Expert", "bg_image": "grand_et_petit.png"},
            {"title": "H8", "level": "Expert", "bg_image": "grand_et_petit.png"},

        ]
        return story_list

    @staticmethod
    def inject_story_in_database(story_list, level_table, story_table):

        for element in story_list:
            level_id = Level.objects.get(name=element["level"]).level_id
            new_story_data = Story(
                level_id=Level.objects.get(level_id=level_id),
                title=element["title"],
                bg_image=element["bg_image"]
            )
            new_story_data.save()

    @staticmethod
    def update_story_table(story_list, level_table, story_table):

        # 1. We extract each story title from story_list
        story_checklist = []
        for element in story_list:
            story_checklist.append(element["title"])

        # 2. We extract each name from story_table
        story_table_checklist = []
        for row in story_table:
            story_table_checklist.append(row.title)
            if row.title not in story_checklist:
                story_table.filter(title=row.title).delete()

        # 3. We check if story title from story_checklist
        # and story title from story_table_checklist both have the same content or not
        for element in story_list:
            if element["title"] not in story_table_checklist:
                level_id = Level.objects.get(name=element["level"])
                new_story_data = Story(
                    level_id=level_id,
                    title=element["title"],
                    bg_image=element["bg_image"]
                )
                new_story_data.save()
