from django.contrib import admin
from django.contrib.auth import get_user_model
from authemail.admin import EmailUserAdmin

from authentication.models import Swimmer, Runner


class SwimmerAdmin(admin.ModelAdmin):
    list_display = (#"email",
                    #"date_of_birth",
                    "position",
                    "meters",
                    "minutes",
                    "strokes",
                    #"city_id",
                    #"name",
                    #"surname",
                    "trend")

#admin.site.unregister(get_user_model())
#admin.site.register(get_user_model(), SwimmerAdmin)
admin.site.register(Swimmer, SwimmerAdmin)

class RunnerAdmin(admin.ModelAdmin):
    list_display = (#"email",
                    #"date_of_birth",
                    "position",
                    "meters",
                    "minutes",
                    #"city_id",
                    #"name",
                    #"surname",
                    "trend")

admin.site.register(Runner, RunnerAdmin)
#admin.site.unregister(get_user_model())
#admin.site.register(get_user_model(), RunnerAdmin)
