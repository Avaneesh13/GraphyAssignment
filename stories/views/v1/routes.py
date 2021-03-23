from rest_framework import routers

from stories.views.v1.story import StoryViewSet

router = routers.SimpleRouter()
router.register(
    r"story", StoryViewSet, basename="story"
)