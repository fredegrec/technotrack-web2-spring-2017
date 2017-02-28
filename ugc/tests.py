from django.test import TestCase
from django.contrib.auth import get_user_model

from events.models import Event
from .models import Post
# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='test_user')
        
    def testPostEvent(self):
        events_count_before = Event.objects.count()
        post = Post.objects.create(author = self.user, text = 'agrbr')
        events_count_after = Event.objects.count()
        self.assertTrue(events_count_before + 1 == events_count_after)
        
        
        
        
    def tearDown(self):
        self.user.delete()
