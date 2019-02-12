from django.contrib import admin

from narwhals.models import SwimWorkout
from narwhals.models import RunWorkout


class SwimWorkoutAdmin(admin.ModelAdmin):
    """
    list_display = ("user",
                    "sport",
                    "difficulty",
                    "duration",
                    "strokes",
                    "distance",
                    "speedAverage",
                    "strokeAverage",
                    "dateStart",
                    "dateFinish")
    """
    pass

admin.site.register(SwimWorkout, SwimWorkoutAdmin)


class RunWorkoutAdmin(admin.ModelAdmin):
    pass

admin.site.register(RunWorkout, RunWorkoutAdmin)

