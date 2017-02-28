from .models import Award
from events.models import Event

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=Award)
def receive_new_award_event(instance, created=False, *args, **kwargs):
    if created:
        Event.objects.create(author=instance.recipient,
                             content_object=instance, 
                             content='{0} получил награду {1}.'.format(instance.recipient, instance.title)
                             )
    

