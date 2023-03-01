from chinese_folktales_website.models import Story, Level

from pathlib import Path
from bs4 import BeautifulSoup
from slugify import slugify
import markdown
import os
import json
import requests


class StoryImporter:
    """
    Import Stories and insert them in the story data table.
    """

    @staticmethod
    def load_story_list():
        stories_data_url = 'https://gist.githubusercontent.com/nicoseng/28a98c1a0e7025479923fab8755c8210/raw/fd77b61176c284b9982a729538ace7f1eba62e0b/stories_data'
        stories_data = requests.get(stories_data_url)
        story_list = stories_data.json()
        print(story_list)
        return story_list

    @staticmethod
    def inject_story_in_database(story_list, level_table, story_table):

        for element in story_list:
            level_id = Level.objects.get(name=element["level"]).level_id
            new_story_data = Story(
                level_id=Level.objects.get(level_id=level_id),
                title=element["title"],
                bg_image=element["bg_image"],
                audiofile=element["audiofile"],
                textfile=element["textfile"],
                audio_bg_image=element["audio_bg_image"],
                description=element["description"]
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
                    bg_image=element["bg_image"],
                    audiofile=element["audiofile"],
                    textfile=element["textfile"],
                    audio_bg_image=element["audio_bg_image"],
                    description=element["description"]
                )
                new_story_data.save()

    @staticmethod
    def open_textfile(textfile_name):
        textfile_basepath = '/Users/nicolassengmany/Desktop/OCR/Python/Projets/P13/chinese_folktales/chinese_folktales_website/stories/texts/'
        story_file = textfile_basepath + textfile_name

        with open(story_file, 'r') as story_content:
            content = story_content.read()
        story_content_html = markdown.markdown(content)
        return story_content_html

    @staticmethod
    def open_audiofile(audiofile_name):
        audiofile_basepath = 'https://github.com/nicoseng/P13_chinese_folktales/blob/0699a2879a5e86756c41b70cace05083a2f55e90/chinese_folktales_website/stories/audio/'
        audio_file = audiofile_basepath + audiofile_name
        return audio_file
