from django.db import models
from django.conf import settings


# creating a new table in database --> make a migration
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # posted_at = models.DateTimeField(default=timezone.now)