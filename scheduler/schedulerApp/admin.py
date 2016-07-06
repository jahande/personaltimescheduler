from django.contrib import admin
from schedulerApp.models import WorkSheet, WorkTime

class WorkTImeAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'end',)
    #search_fields = ('name',)
    list_filter = ('name',)
    date_hierarchy = 'start'

admin.site.register(WorkSheet)
admin.site.register(WorkTime, WorkTImeAdmin)