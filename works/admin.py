from django.contrib import admin
from .models import WeeklyReport, PostDocReport
# Register your models here.


class WeeklyReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'writer',)
    # search_fields = ['name', 'position']

class PostDocReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'writer')
    
admin.site.register(WeeklyReport, WeeklyReportAdmin)
admin.site.register(PostDocReport, PostDocReportAdmin)