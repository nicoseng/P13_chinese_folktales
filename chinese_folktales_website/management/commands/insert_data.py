from django.core.management.base import BaseCommand
from chinese_folktales_website.level_importer import LevelImporter
from chinese_folktales_website.story_importer import StoryImporter
from chinese_folktales_website.models import Level, Story


class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.level_table = Level.objects.all()
        self.story_table = Story.objects.all()

        self.level_imported = LevelImporter()
        self.level_list = self.level_imported.load_level_list()

        self.story_imported = StoryImporter()
        self.story_list = self.story_imported.load_story_list()

    def handle(self, *args, **options):

        # Levels insertion
        if Level.objects.count() == 0:
            self.level_imported.inject_level_in_database(self.level_list)
            self.stdout.write("Données niveaux insérées.")

        # Levels updating
        else:
            self.level_imported.update_level_table(self.level_list, self.level_table)
            self.stdout.write("Mise à jour niveaux effectuée.")

        # Stories insertion
        if Story.objects.count() == 0:
            self.story_imported.inject_story_in_database(self.story_list, self.level_table, self.story_table)
            self.stdout.write("Données histoires bien insérées.")

        # Stories updating
        else:
            self.story_imported.update_story_table(self.story_list, self.level_table, self.story_table)
            self.stdout.write("Mise à jour des histoires effectuée.")
