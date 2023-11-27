from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class DuplicateHandler(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    original_object_id = models.PositiveIntegerField()
    original = GenericForeignKey('content_type', 'original_object_id')
    replacement_object_id = models.PositiveIntegerField()
    replacement = GenericForeignKey('content_type', 'replacement_object_id')

    def __str__(self):
        return f'{self.content_type}'