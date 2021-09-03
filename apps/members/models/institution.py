"""Members app models"""
from django.db import models

from apps.models.commons import SoftDeletionModel


class Institution(SoftDeletionModel):
    """Members Institution model class"""
    name = models.CharField(max_length=64, db_index=True)
    old_name = models.CharField(max_length=64, db_index=True)
    slug = models.CharField(max_length=128)

    @property
    def is_active(self):
        return self.deleted_at is None

    def __str__(self):
        return self.name
