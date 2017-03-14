from .models import Request, FriendShip
from events.models import Event

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver




       