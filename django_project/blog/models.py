from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse

# Function to validate that the uploaded file is an image, audio, or video
def validate_media_file(value):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.mp3', '.wav', '.mp4', '.avi', '.mov', '.wmv']
    ext = value.name.split('.')[-1].lower()
    if f'.{ext}' not in valid_extensions:
        raise ValidationError(f'Unsupported file extension. Allowed extensions: {", ".join(valid_extensions)}')

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    media = models.FileField(upload_to='post_media/', null=True, blank=True, validators=[validate_media_file])  # Single media field
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
