from django.conf.urls import url
from django.urls import include

from stories.views.v1.routes import router as router_v1

urlpatterns = [
    url(r"^v1/", include(router_v1.urls)),
]
