from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# creating a new table in database --> make a migration
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True) 
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    # social links
    website = models.CharField(max_length=80, blank=True)
    facebook = models.CharField(max_length=80, blank=True)
    instagram = models.CharField(max_length=80, blank=True)
    twitter = models.CharField(max_length=80, blank=True)
    discord = models.CharField(max_length=80, blank=True)
    github = models.CharField(max_length=80, blank=True)
    linkedin = models.CharField(max_length=80, blank=True)
    youtube = models.CharField(max_length=80, blank=True)
    spotify = models.CharField(max_length=80, blank=True)


    # # personal info
    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()