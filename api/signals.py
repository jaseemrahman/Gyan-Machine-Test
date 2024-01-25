from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from api.models import Gallery
from api.helper import ImageConverter


@receiver(post_save, sender=Gallery)
def convet_image(sender, instance, created, **kwargs):
    if created:
        if instance.image:
            input_path = os.path.abspath(instance.image.path)
            try:
                res=ImageConverter.convert_to_webp(input_path)
                instance.image.name = os.path.relpath(res, 'media')
                instance.save(update_fields=['image'])
                os.remove(input_path)
            except Exception as e:
                print(str(e))

