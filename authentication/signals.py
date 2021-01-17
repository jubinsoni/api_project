from django.db.models.signals import post_save
from django.dispatch import receiver

from user_profile.models import UserProfile

from .models import User


@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, *args, **kwargs):
    if instance and created:
        instance.profile = UserProfile.objects.create(user=instance)