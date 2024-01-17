from django.contrib import admin

# Register your models here.

from .models import Serendipity

class SerendipityAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'writer')
    list_filter = ['write_date']

admin.site.register(Serendipity, SerendipityAdmin)