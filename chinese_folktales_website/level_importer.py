from chinese_folktales_website.models import Level


class LevelImporter:
    """
    Import Levels and insert it in the level database table.
    """

    @staticmethod
    def load_level_list():

        level_list = [
            {"name": "Facile"},
            {"name": "Moyen"},
            {"name": "Difficile"},
            {"name": "Expert"}
        ]
        return level_list

    @staticmethod
    def inject_level_in_database(level_list):
        for element in level_list:
            level_data = Level(
                name=element["name"],
            )
            level_data.save()
        level_table = Level.objects.all()
        return level_table

    @staticmethod
    def update_level_table(level_list, level_table):

        """
        Compare two lists and logs the difference.
        :param level_list: first list.
        :param level_table: second list.
        :return: if there is difference between both lists.
        """

        level_table_list = list(Level.objects.values('name'))

        for i in level_list:
            if i not in level_table_list:
                level_table_list.append(i)
                level_data = Level(
                    name=i["name"]
                )
                level_data.save()

        for j in level_table_list:
            if j not in level_list:
                level_table_list.remove(j)
                Level.objects.get(name=j["name"]).delete()

        level_table = Level.objects.all()
        return level_table
