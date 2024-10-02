from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
import os

# Signal to create a profile when a user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Signal to save the profile when a user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# Signal to delete the profile picture from the file system when the profile is deleted
@receiver(post_delete, sender=Profile)
def delete_profile_image(sender, instance, **kwargs):
    if instance.image and instance.image.path != 'profile_pics/default.jpg':
        # Ensure the default image is not deleted
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
