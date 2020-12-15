from django.db import models

# creating a new table in database --> make a migration
class Note(model.Model):
    title = model.CharField(max_length = 200)
    body = models.TextField()