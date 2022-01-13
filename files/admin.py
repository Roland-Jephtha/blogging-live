from django.contrib import admin
from . import models
class FileAdmin(admin.ModelAdmin):
    list_display = ('title', )
# Register your models here.
admin.site.register(models.File, FileAdmin)