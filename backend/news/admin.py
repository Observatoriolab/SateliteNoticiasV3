from django.contrib import admin
from .models import Edition, News,Comment
# Register your models here.

admin.site.register(Edition)
admin.site.register(News)
admin.site.register(Comment)