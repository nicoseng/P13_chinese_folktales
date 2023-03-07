from chinese_folktales_website.models import Favorite


class StoryEliminator:
    """Eliminates story datas in Favorite database"""

    @staticmethod
    def delete_story(story_id):
        favorite_database = Favorite.objects.all()
        story_selected = Favorite.objects.get(story_id=story_id)
        story_selected.delete()

        favorite_database.update()
        return favorite_database
