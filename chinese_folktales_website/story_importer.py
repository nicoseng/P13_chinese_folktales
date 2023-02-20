from chinese_folktales_website.models import Story, Level
from os import path
from bs4 import BeautifulSoup
from slugify import slugify
import markdown


class StoryImporter:
    """
    Import Stories and insert them in the story data table.
    """

    @staticmethod
    def load_story_list():

        # open a file
        file_path = path.relpath("/Users/nicolassengmany/Desktop/OCR/Python/Projets/P13/chinese_folktales/chinese_folktales_website/stories/兩隻小兔/兩隻小兔.md")
        with open(file_path) as file1:
            # read the file
            read_content = file1.read()
            print(read_content)

        html = markdown.markdown(read_content)
        print(html)

        s = BeautifulSoup(html, 'html.parser')
        for title in s.find_all("h1"):
            section = s.new_tag("section")
            section.string = title.string
            section.attrs['id'] = slugify(title.string)
            title.replace_with(section)

        print(section)

        # Récupérer à partir de github (extraire les données ici)
        story_list = [
            {"title": "H1", "level": "Débutant"},
            {"title": "H2", "level": "Débutant+"},
            {"title": "H3", "level": "Intermédiaire"},
            {"title": "H4", "level": "Intermédiaire+"},
            {"title": "H5", "level": "Avancé"},
            {"title": "H6", "level": "Avancé+"},
            {"title": "H7", "level": "Expert"},
        ]
        return story_list

    @staticmethod
    def inject_story_in_database(story_list, level_table, story_table):

        for element in story_list:
            level_id = Level.objects.get(name=element["level"]).level_id
            new_story_data = Story(
                level_id=Level.objects.get(level_id=level_id),
                title=element["title"])
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
                    title=element["title"]
                )
                new_story_data.save()
