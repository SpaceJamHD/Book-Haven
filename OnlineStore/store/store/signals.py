from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Comment, Item

@receiver(post_save, sender=Comment)
@receiver(post_delete, sender=Comment)
def update_item_average_rating(sender, instance, **kwargs):
    instance.item.update_average_rating()
