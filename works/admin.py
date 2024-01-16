from django.contrib import admin
from .models import WeeklyReport, PostDocReport
# Register your models here.


class WeeklyReportAdmin(admin.ModelAdmin):
    list_display = ('is_post_doc', 'user', 'writer',)
    list_filter = ('is_post_doc',)
    # search_fields = ['name', 'position']

class PostDocReportAdmin(admin.ModelAdmin):
    list_display = ('user',)
    
admin.site.register(WeeklyReport, WeeklyReportAdmin)
admin.site.register(PostDocReport, PostDocReportAdmin)