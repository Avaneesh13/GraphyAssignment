from django.db import models

from GraphyAssignment.utility.models import TimeStampedModel
from stories.constants import STORY_TYPE_CHOICES


class Stories(TimeStampedModel):
    grapher = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    type = models.CharField(
        max_length=1,
        choices=STORY_TYPE_CHOICES,
    )
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StoriesToProcess(models.Model):
    pass
