from django.contrib import admin

from stories.models import Story


class StoriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Story._meta.fields]


admin.site.register(Story, StoriesAdmin)
