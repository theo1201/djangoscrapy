from django.contrib import admin

# Register your models here.
from .models import TheodoTeam

class TheodoTeamAdmin(admin.ModelAdmin):
    list_display=('text', 'author', 'id')

admin.site.register(TheodoTeam,TheodoTeamAdmin)