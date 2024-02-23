from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shared_with = models.ManyToManyField(User, related_name='shared_notes', blank=True)

    def __str__(self):
        return self.title

class NoteVersion(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Version of {self.note.title} at {self.created_at}"
