from django.db import models
from accounts.models import CustomUser


class Note(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=100)
    description = models.TextField()
    attachment = models.FileField(upload_to="attachments/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
