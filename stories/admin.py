from django.contrib import admin

from stories.models import Stories


class StoriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Stories._meta.fields]


admin.site.register(Stories, StoriesAdmin)
