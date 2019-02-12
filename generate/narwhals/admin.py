from django.contrib import admin

from narwhals.models import Entrenamiento

class EntrenamientoAdmin(admin.ModelAdmin):
    list_display = ("user", "sport", "filepath", "isPrivate", "isSynchronized", "difficulty")

admin.site.register(Entrenamiento, EntrenamientoAdmin)
