from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'backend.news'
    verbose_name= 'News'
    
    def ready(self):
        import backend.news.signals