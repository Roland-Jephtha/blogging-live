from django.contrib import admin
from . import models
from .models import Post, Category,Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')

class CommentAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(models.Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)


