from django.contrib import admin
from .models import Story, Level, Favorite


class StoryAdmin(admin.ModelAdmin):
    list_display = ('story_id',
                    'title',
                    'chinese_title',
                    'bg_image',
                    'level_id',
                    'textfile',
                    'audiofile',
                    'description',
                    'audio_bg_image',
                    'date'
                    )


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user_id',
                    'story_id'
                    )


class LevelAdmin(admin.ModelAdmin):
    list_display = ('level_id',
                    'name'
                    )


admin.site.register(Story, StoryAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Level, LevelAdmin)
