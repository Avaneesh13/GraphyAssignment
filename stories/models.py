from django.core.validators import FileExtensionValidator
from django.db import models, transaction

from GraphyAssignment.utility.models import TimeStampedModel
from stories.constants import STORY_TYPE_CHOICES
from stories.tasks import optimize_image, optimize_video


class Story(TimeStampedModel):
    grapher = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    content = models.FileField(
        upload_to='content',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'mp4'])]
    )
    content_type = models.CharField(
        max_length=1,
        choices=STORY_TYPE_CHOICES,
    )
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Story, self).save(*args, **kwargs)
        if self.content:
            if int(self.content_type) == 1:
                transaction.on_commit(lambda: optimize_image.delay(self.content.path))
            elif int(self.content_type) == 2:
                transaction.on_commit(lambda: optimize_video.delay(self.content.path))
