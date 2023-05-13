from django.db.models.signals import post_save
from django.dispatch import receiver
from newsapp.tasks import task_create_notify
from newsapp.models import Post


@receiver(post_save, sender=Post)
def post_created_notify(instance, created, **kwargs):
    if not created:
        return
    task_create_notify.delay(instance.id)
