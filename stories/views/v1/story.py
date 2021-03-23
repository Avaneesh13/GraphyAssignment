from rest_framework import viewsets, mixins

from stories.models import Story
from stories.views.v1.serializer import StorySerializer


class StoryViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):

    serializer_class = StorySerializer
    queryset = Story.objects.all().order_by("created_on")
