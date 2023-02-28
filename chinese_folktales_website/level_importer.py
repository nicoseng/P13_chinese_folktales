from chinese_folktales_website.models import Level


class LevelImporter:
    """
    Import Levels and insert it in the level database table.
    """

    @staticmethod
    def load_level_list():

        level_list = [
            {"level": "Facile"},
            {"level": "Moyen"},
            {"level": "Difficile"},
            {"level": "Expert"},
        ]
        return level_list

    @staticmethod
    def inject_level_in_database(level_list):
        for element in level_list:
            level_data = Level(
                name=element["level"],
            )
            level_data.save()

    @staticmethod
    def update_level_table(level_list, level_table):

        # 1. We extract each level from level_list
        level_checklist = []
        for element in level_list:
            level_checklist.append(element["level"])

        # 2. We extract each level from level_table_list
        level_table_checklist = []
        for level in level_table:
            level_table_checklist.append(level.name)
            if level.name not in level_checklist:
                level_table.filter(name=level.name).delete()

        # 3. We check if level from level_checklist
        # and level from level_table_checklist both have the same content or not
        for element in level_checklist:
            if element not in level_table_checklist:
                level_data = Level(
                    name=element
                )
                level_data.save()
