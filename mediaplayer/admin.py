from django.contrib import admin

# Register your models here.
from mediaplayer.models import Show, Creator, Genre, Studio, Season, Episode, Video

class SeasonInline(admin.StackedInline):
	model = Season
	extra = 1


class ShowAdmin(admin.ModelAdmin):
	inlines = [SeasonInline]


admin.site.register(Show, ShowAdmin)
admin.site.register(Creator)
admin.site.register(Genre)
admin.site.register(Studio)
admin.site.register(Episode)
# Below is library / meta stuff?
admin.site.register(Video)