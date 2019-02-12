from django.contrib import admin

from authentication.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("email",
                    "date_of_birth",
                    "position",
                    "meters",
                    "minutes",
                    "strokes",
                    "metersAverage",
                    "minutesAverage",
                    "city_id",
                    "name",
                    "surname",
                    "trend")

admin.site.register(User, UserAdmin)
