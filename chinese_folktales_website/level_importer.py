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

        print("level_list:", level_list)
        level_table_list = list(Level.objects.values('name'))
        print("level_table_list :", level_table_list)

        for i in level_list:
            if i not in level_table_list:
                print("Element différent:", i)
                level_table_list.append(i)
                level_data = Level(
                    name=i["name"]
                )
                level_data.save()

        for j in level_table_list:
            if j not in level_list:
                level_table_list.remove(j)
                Level.objects.get(name=j["name"]).delete()

        print("Liste nettoyée:", level_table_list)

        # # 1. We extract each level from level_list
        # level_checklist = []
        # for element in level_list:
        #     level_checklist.append(element["name"])
        #
        # level_table_checklist = []
        # # 2. We extract each level from level_table_checklist
        # for item in level_table_list:
        #     level_table_checklist.append(item["name"])
        #
        # print("level_checklist", level_checklist)
        # print("level_table_checklist", level_table_checklist)
        #
        # for element in level_checklist:
        #     if element not in level_table_checklist:
        #         level_data = Level(
        #             name=element
        #         )
        #         level_data.save()
        #
        # for row in level_table:
        #     if row.name not in level_checklist:
        #         level_table.filter(name=row.name).delete()

        # # 2. We extract each level from level_table_checklist
        # for level in level_table_checklist:
        #     if level["name"] not in level_checklist:
        #         level_table.filter(name=level["name"]).delete()
        #
        # # 3. We check if level from level_checklist
        # # and level from level_table_checklist both have the same content or not
        # for element in level_checklist:
        #     if element not in level_table_checklist:
        #         level_data = Level(
        #             name=element
        #         )
        #         level_data.save()
        #
        level_table = Level.objects.all()
        return level_table
