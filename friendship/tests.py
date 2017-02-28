from django.test import TestCase
from django.contrib.auth import get_user_model

from events.models import Event
from .models import Request, FriendShip
# Create your tests here.
class FriendShipTestCase(TestCase):
    def setUp(self):
        self.first = get_user_model().objects.create(username='test_friend1')
        self.second = get_user_model().objects.create(username='test_friend2')
        
    def testCreateFriendShip(self):
        self.request=Request.objects.create(author = self.first, recipient=self.second)
        friendship_obj_count_before=FriendShip.objects.count()
        events_count_before = Event.objects.count()
        self.request.accepted=True
        request.save()
        friendship_obj_count_after=FriendShip.objects.count()
        events_count_after = Event.objects.count()
        self.assertTrue(friendship_obj_count_before + 2 == friendship_obj_count_after, msg="friendship, ok")
        self.assertTrue(events_count_before + 2 == events_count_after, msg = "event, ok")
        
               
        
    def tearDown(self):
        self.first.delete()
        self.second.delete()