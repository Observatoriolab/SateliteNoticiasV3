from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from backend.core.utils import generate_random_string
from backend.news.models import News

@receiver(pre_save, sender=News)
def add_slug_to_news(sender,instance,*args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string
