from django.contrib import admin

from stats.models import RunningStats, SwimmingStats


class RunningStatsAdmin(admin.ModelAdmin):
    pass

admin.site.register(RunningStats, RunningStatsAdmin)


class SwimmingStatsAdmin(admin.ModelAdmin):
    pass

admin.site.register(SwimmingStats, SwimmingStatsAdmin)

