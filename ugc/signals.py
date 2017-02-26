from .models import Post
from events.models import Event

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Post)
def created_post_event(instance, created=False, *args, **kwargs):
    if created:
        Event.object.create(author=instance.author, 
                            content_object = instance,
                            content='{0} опубликовал пост "{1}".\n{2}'.format(instance.author, instance.title, instance.text)
                             )

        