from django.core.management.base import BaseCommand
from chinese_folktales_website.story_importer import StoryImporter
from chinese_folktales_website.models import Story


class Command(BaseCommand):

    def handle(self, *args, **options):
        story_table = Story.objects.all()
        if len(story_table) == 0:

            try:
                story_imported = StoryImporter()
                story_list = story_imported.load_story_list()
                story_imported.inject_story_in_database(story_list)

            except:
                Story.objects.all()
            self.stdout.write("Histoires bien importées.")

        else:
            self.stdout.write("Histoires déjà importées.")
