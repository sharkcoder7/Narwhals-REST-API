from django.contrib import admin
from django.contrib.auth import get_user_model
from authemail.admin import EmailUserAdmin

from authentication.models import Swimmer, Runner


class SwimmerAdmin(admin.ModelAdmin):
    list_display = ('email',
                    'position',
                    'meters',
                    'minutes',
                    'strokes',
                    'trend')

    readonly_fields = ('email',)

    def email(self, obj):
        return obj.type.email


admin.site.register(Swimmer, SwimmerAdmin)

class RunnerAdmin(admin.ModelAdmin):
    list_display = ('email',
                    'position',
                    'meters',
                    'minutes',
                    'trend')

    readonly_fields = ('email',)

    def email(self, obj):
        return obj.type.email

admin.site.register(Runner, RunnerAdmin)
