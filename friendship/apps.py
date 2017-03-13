from __future__ import unicode_literals

from django.apps import AppConfig


class FriendshipConfig(AppConfig):
    name = 'friendship'
    
    def ready(self):
        import api
        import signals
        import views
