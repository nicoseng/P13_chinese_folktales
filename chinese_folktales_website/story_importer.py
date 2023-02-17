from chinese_folktales_website.models import Story, Level
from django.core.exceptions import ObjectDoesNotExist

class StoryImporter:
    """
    Import Stories and insert them in the story data table.
    """

    @staticmethod
    def load_story_list():
        # Récupérer à partir de github (extraire les données ici)
        story_list = [
            {"title": "H1", "level": "Débutant"},
            {"title": "H2", "level": "Débutant+"},
            {"title": "H3", "level": "Intermédiaire"},
            {"title": "H4", "level": "Intermédiaire+"},
            {"title": "H5", "level": "Intermédiaire+"},
            {"title": "H6", "level": "Avancé+"},
            {"title": "H7", "level": "Débutant+"},
            {"title": "H8", "level": "Expert"},
            {"title": "H9", "level": "Intermédiaire"},
            {"title": "H10", "level": "Intermédiaire+"},
        ]
        return story_list

    @staticmethod
    def inject_story_in_database(story_list, level_table, story_table):

        for element in story_list:
            try:
                story_data = Story.objects.get(title=element["title"])
                print(story_data)
            except ObjectDoesNotExist:
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



















        # # 1. We extract each story from story_list
        # story_checklist = []
        # for element in story_list:
        #     story_checklist.append(element["level"])
        # print("story_checklist:", story_checklist)
        #
        # # 2. We extract each story from story_table
        # story_table_checklist = []
        # for story in story_table:
        #     story_table_checklist.append(story.title)
        #     if story.title not in story_checklist:
        #         story_table.filter(title=story.title).delete()
        # print("story_table:", story_table)
        # print("story_table_checklist:", story_table_checklist)

        # 3. We check if story from story_checklist
        # and story from story_table_checklist are the same or not
        # for element in story_list:
        #     print(element["title"])
        #     level_id = Level.objects.get(name=element["title"]).level_id
        #     print(level_id)
        #     if element["title"] not in story_table_checklist:
        #         pass
        #         # level_id = Level.objects.get(name=element["name"]).level_id
        #         # print(level_id)
        #         # story_data = Story(
        #         #     level_id=Level.objects.get(name=element["name"]),
        #         #     title=element["title"]
        #         # )
        #         # story_data.save()
        #
        # story_table = Story.objects.all()
        # print("story_table:", story_table)
        # return story_table
