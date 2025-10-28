from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import Note
import os


@receiver(post_delete, sender=Note)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.attachment:
        if os.path.isfile(instance.attachment.path):
            os.remove(instance.attachment.path)
