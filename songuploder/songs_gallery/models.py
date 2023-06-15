from django.db import models
from auth_app.models import User

# Create your models here.
class UploadedSongs(models.Model):
    user_email = models.ForeignKey(User, on_delete=models.CASCADE, to_field='email')
    song_key = models.CharField(max_length=255)
    song_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return {"song_key": self.song_key, "user_email": self.user_email}
    





class Audio(models.Model):
    ENUM_CHOICES = [
        ('Protected', 'Protected'),
        ('Private', 'Private'),
        ('Public', 'Public'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio/')
    access_type = models.CharField(max_length=20, choices=ENUM_CHOICES)
    

class ProtectedFileAccess(models.Model):
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('audio', 'user')