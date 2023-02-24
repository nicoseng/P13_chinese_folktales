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
        stories_data_url = 'https://gist.githubusercontent.com/nicoseng/28a98c1a0e7025479923fab8755c8210/raw/7faff30eedd0b7e917243eb464f9f315081ed593/stories_data'
        stories_data = requests.get(stories_data_url)
        print(stories_data)
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
                # images=element["images"],
                audiofile=element["audiofile"],
                textfile=element["textfile"]
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
                )
                new_story_data.save()
