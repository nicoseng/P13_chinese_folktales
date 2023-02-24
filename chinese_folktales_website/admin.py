from django.contrib import admin
from .models import Story, Level, Favourite, Comment


class StoryAdmin(admin.ModelAdmin):
    list_display = ('story_id',
                    'title',
                    'images',
                    'level_id',
                    'textfile',
                    'audiofile',
                    'date'
                    )


class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user_id',
                    'story_id'
                    )


class LevelAdmin(admin.ModelAdmin):
    list_display = ('level_id',
                    'name'
                    )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_id',
                    'story_id',
                    'comment',
                    'rating',
                    'date'
                    )


admin.site.register(Story, StoryAdmin)
admin.site.register(Favourite, FavouriteAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Comment, CommentAdmin)
