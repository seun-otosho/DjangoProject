"""Members app models"""
from django.db import models


class Institution(models.Model):
    """Members Institution model class"""
    name = models.CharField(max_length=64, db_index=True)
    old_name = models.CharField(max_length=64, db_index=True)
