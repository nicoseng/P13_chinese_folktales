from chinese_folktales_website.models import Story, Level
from pathlib import Path
from markdown import markdown
import os
import json
import requests


class StoryImporter:
    """
    Import Stories and insert them in the story data table.
    """

    @staticmethod
    def load_story_list():
        stories_data_url = 'https://gist.githubusercontent.com/nicoseng/28a98c1a0e7025479923fab8755c8210/raw/a11aabb0b28380d66f53543d5abc6710c195ba13/stories_data'
        stories_data = requests.get(stories_data_url)
        story_list = stories_data.json()
        return story_list

    @staticmethod
    def inject_story_in_database(story_list, level_table, story_table):

        for element in story_list:
            level_id = Level.objects.get(name=element["level"]).level_id
            new_story_data = Story(
                level_id=Level.objects.get(level_id=level_id),
                title=element["title"],
                chinese_title=element["chinese_title"],
                bg_image=element["bg_image"],
                audiofile=element["audiofile"],
                textfile=element["textfile"],
                audio_bg_image=element["audio_bg_image"],
                description=element["description"]
            )
            new_story_data.save()
        story_table = Story.objects.all()
        return story_table

    @staticmethod
    def update_story_table(story_list, level_table, story_table):

        """
        Compare two lists and logs the difference.
        :param story_list: first list.
        :param level_table
        :param story_table: second list.
        :return: if there is difference between both lists.
        """

        # print("story_list:", story_list)
        # story_table_list = list(Story.objects.values('title','chinese_title',''))
        # print("story_table_list :", story_table_list)
        # if story_table_list == story_list:
        #     print("pareil")
        # else:
        #     print("pas pareil")

        # for i in story_list:
        #     if i not in story_table_list:
        #         print("Element différent:", i)
        #         story_table_list.append(i)
        #         level_id = Level.objects.get(name=i["level"])
        #         new_story_data = Story(
        #             level_id=level_id,
        #             title=i["title"],
        #             chinese_title=i["chinese_title"],
        #             bg_image=i["bg_image"],
        #             audiofile=i["audiofile"],
        #             textfile=i["textfile"],
        #             audio_bg_image=i["audio_bg_image"],
        #             description=i["description"]
        #         )
        #         new_story_data.save()
        #
        # for j in story_table_list:
        #     if j not in story_list:
        #         story_table_list.remove(j)
        #         Story.objects.get(title=j["title"]).delete()
        #
        # story_table = Story.objects.all()
        # return story_table





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
                    chinese_title=element["chinese_title"],
                    bg_image=element["bg_image"],
                    audiofile=element["audiofile"],
                    textfile=element["textfile"],
                    audio_bg_image=element["audio_bg_image"],
                    description=element["description"]
                )
                new_story_data.save()
        story_table = Story.objects.all()
        return story_table

    @staticmethod
    def open_textfile(textfile_name):
        textfile_basepath = '/Users/nicolassengmany/Desktop/OCR/Python/Projets/P13/chinese_folktales/chinese_folktales_website/stories/texts/'
        story_file = textfile_basepath + textfile_name

        with open(story_file, 'r') as story_content:
            content = story_content.read()
        story_content_html = markdown(content)
        return story_content_html
