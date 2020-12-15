from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# creating a new table in database --> make a migration
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True) 
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title