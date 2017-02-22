from django.contrib import admin
from .models import Post, Comment
from likes.admin import LikeInline

from django.contrib.contenttypes.admin import GenericInlineModelAdmin
# Register your models here.

#class CommentInline(admin.TabularInline):
#    model = Comment
class CommentInline(admin.StackedInline, GenericInlineModelAdmin):
    model = Comment
    ct_field = 'content_type'
    ct_fk_field = 'object_id'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = CommentInline, LikeInline,