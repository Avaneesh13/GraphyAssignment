from rest_framework import viewsets, mixins

from stories.models import Story
from stories.views.v1.serializer import StorySerializer


class StoryViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):

    serializer_class = StorySerializer
    queryset = Story.objects.all()
