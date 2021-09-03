"""Members app models"""
from django.db import models

from apps.models.commons import SoftDeletionModel


class Institution(SoftDeletionModel):
    """Members Institution model class"""
    name = models.CharField(max_length=64, db_index=True)
    old_name = models.CharField(max_length=64, db_index=True)

    def __str__(self):
        return self.name
