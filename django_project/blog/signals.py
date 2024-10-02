from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Post
import os

@receiver(post_delete, sender=Post)
def delete_media_file(sender, instance, **kwargs):
    """ Deletes media file associated with a post when the post is deleted. """
    if instance.media:  # If the post has an associated media file
        media_path = instance.media.path  # Get the file path of the media
        if os.path.isfile(media_path):  # Check if the file exists
            os.remove(media_path)  # Delete the file from the file system
