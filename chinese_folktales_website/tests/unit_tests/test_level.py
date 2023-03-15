from django.test import TestCase
from chinese_folktales_website.level_importer import LevelImporter
from chinese_folktales_website.models import Level


class TestLevel(TestCase):

    def setUp(self):
        self.level_importer = LevelImporter()
        self.test_level_list = [
            {"name": "Facile"},
            {"name": "Moyen"},
            {"name": "Difficile"},
            {"name": "Expert"},
        ]

    def test_extract_level(self):
        level_list_loaded = self.level_importer.load_level_list()
        expected_results = [
            {"name": "Facile"},
            {"name": "Moyen"},
            {"name": "Difficile"},
            {"name": "Expert"},
        ]
        assert expected_results == level_list_loaded

    def test_inject_level_in_database(self):
        Level.objects.bulk_create([
            Level(level_id=1, name="Facile"),
            Level(level_id=2, name="Moyen"),
            Level(level_id=3, name="Difficile")
        ])
        test_results = self.level_importer.inject_level_in_database(self.test_level_list)
        expected_results = Level.objects.all()
        assert len(test_results) == len(expected_results)

    def test_update_level_table_1(self):
        test_level_list = [
            {"name": "Facile"},
            {"name": "Moyen"},
            {"name": "Difficile"},
            {"name": "Expert"},
        ]
        test_level_table = Level.objects.bulk_create([
            Level(level_id=1, name="Facile"),
            Level(level_id=2, name="Moyen"),
            Level(level_id=3, name="Difficile")
        ])
        test_results = self.level_importer.update_level_table(test_level_list, test_level_table)
        expected_results = Level.objects.values()
        assert test_results.values()[0] == expected_results[0]
        assert test_results.values()[1] == expected_results[1]
        assert test_results.values()[2] == expected_results[2]

    def test_update_level_table_2(self):
        test_level_list = [
            {"name": "Facile"},
            {"name": "Moyen"},
            {"name": "Difficile"},
        ]
        test_level_table = Level.objects.bulk_create([
            Level(level_id=1, name="Facile"),
            Level(level_id=2, name="Moyen"),
            Level(level_id=3, name="Difficile"),
            Level(level_id=4, name="Expert")
        ])
        test_results = self.level_importer.update_level_table(test_level_list, test_level_table)
        print(test_results)
        expected_results = Level.objects.values()

        print(expected_results)
        assert test_results.values()[0] == expected_results[0]
        assert test_results.values()[1] == expected_results[1]
        assert test_results.values()[2] == expected_results[2]
