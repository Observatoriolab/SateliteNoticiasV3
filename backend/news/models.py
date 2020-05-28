from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

# Create your models here.
class News(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=240,blank=True)
    content = models.TextField(blank=True)
    fullContent = models.TextField(blank=True)
    relevance = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="relevance")
    irrelevance = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="irrelevance")

    bibliography_name = models.TextField(blank=True)
    bibliography_link = models.TextField(blank=True)
    # Pseudo ID to retrieve the details of a single news
    slug = models.SlugField(max_length=255, unique=True)

    authors = models.TextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="news")
    tags = TaggableManager(blank = True) 


    relevanceData = models.TextField(blank=True)
    irrelevanceData = models.TextField(blank=True)

    relevanceAccumulated = models.BigIntegerField(default=0)
    irrelevanceAccumulated = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title

class Edition(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=240)
    #cambio nuevo
    bibliography_name = models.TextField(blank=True)
    bibliography_link = models.TextField(blank=True)
    #cambio nuevo

    body = models.TextField()


    news = models.ForeignKey(News,
                                on_delete=models.CASCADE,
                                related_name="editions")

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="votes")

    tags = TaggableManager(blank = True) 

    def __str__(self):
        return self.author.username


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    news = models.ForeignKey(News,
                                on_delete=models.CASCADE,
                                related_name="comments")

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="votesComments")


    def __str__(self):
        return self.author.username

