from .models import Request, FriendShip
from events.models import Event

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=Request)
def accept_friends_request(instance, *args, **kwargs):
    if instance.accepted:
        FriendShip.objects.create(first=instance.author,second=instance.recipient)
        FriendShip.objects.create(first=instance.recipient,second=instance.author)
        
        
@receiver(post_save, sender=FriendShip)
def created_friendship_event(instance, created = False, *args, **kwargs):
    if created:
        Event.objects.create(author=instance.first,
                             content_object=instance, 
                             content='{0} и {1} стали друзьями.'.format(instance.first, instance.second)
                             )
                     
@receiver(post_delete, sender=FriendShip)
def delete_friend(instance, *args, **kwargs):
    FriendShip.objects.filter(first=instance.second, second=instance.first).delete()
    
