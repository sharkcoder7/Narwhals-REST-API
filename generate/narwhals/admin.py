from django.contrib import admin

from narwhals.models import Workout

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("user", "sport", "difficulty", "duration", "strokes", "distance", "speedAverage", "strokeAverage")

admin.site.register(Workout, WorkoutAdmin)
