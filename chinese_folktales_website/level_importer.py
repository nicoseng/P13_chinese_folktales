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
        nb_of_level = len(level_list)
        num_id = 1
        while num_id < nb_of_level:
            for element in level_list:
                level_data = Level(
                    level_id=num_id,
                    name=element["name"],
                )
                level_data.save()
                num_id = num_id + 1
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
        num_id = 1
        for i in level_list:
            if i not in level_table_list:
                level_table_list.append(i)
                level_data = Level(
                    level_id=num_id,
                    name=i["name"]
                )
                level_data.save()
                num_id = num_id + 1

        for j in level_table_list:
            if j not in level_list:
                level_table_list.remove(j)
                Level.objects.get(name=j["name"]).delete()

        level_table = Level.objects.all()
        return level_table
