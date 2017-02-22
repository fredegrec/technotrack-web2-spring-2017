from django.contrib import admin

# Register your models here.
from django.contrib.contenttypes.admin import GenericInlineModelAdmin
from .models import Like

class LikeInline(admin.StackedInline, GenericInlineModelAdmin):
    model = Like
    ct_field = 'content_type'
    ct_fk_field = 'object_id'

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass

