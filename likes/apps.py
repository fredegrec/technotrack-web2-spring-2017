from __future__ import unicode_literals

from django.apps import AppConfig


class LikesConfig(AppConfig):
    name = 'likes'
    
    def ready(self):
        import api
        import views
