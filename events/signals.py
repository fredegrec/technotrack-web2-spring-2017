from .models import Eventable

from django.db.models.signals import post_save
from .models import Event, Eventable


def create_event(instance, created = False, *args, **kwargs):
    if created:
        Event.objects.create(author=instance.get_author(),
                             content_object=instance
                             )


for model in Eventable.__subclasses__():
    post_save.connect(create_event, sender = model)