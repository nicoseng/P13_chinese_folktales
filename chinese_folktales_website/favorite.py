from django.contrib.auth.models import User
from chinese_folktales_website.models import Story, Favorite


class StoryInFavorite:
    """To inject products datas in favourite database """

    @staticmethod
    def inject_story_in_favorite(story_selected, user_id):

        favorite_database = Favorite.objects.all()
        current_user = User.objects.get(id=user_id)

        if Favorite.objects.filter(story_id=story_selected).exists():
            return favorite_database
        else:
            story_id = Story.objects.get(story_id=story_selected)
            story_selected_data = Favorite(
                user_id=current_user,
                story_id=story_id
            )
            story_selected_data.save()
            favorite_database = Favorite.objects.filter(user_id=user_id)
            favorite_database.update()
        return favorite_database

    @staticmethod
    def retrieve_favorite_database(user_id):
        favorite_database = Favorite.objects.all()
        favorite_database = favorite_database.filter(user_id=user_id)
        return favorite_database
