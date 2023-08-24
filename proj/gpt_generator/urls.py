from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import GeneratedImageViewSet, GeneratedResponseViewSet

router = DefaultRouter()
router.register(r"generated-responses", GeneratedResponseViewSet)
router.register(r"generated-images", GeneratedImageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
