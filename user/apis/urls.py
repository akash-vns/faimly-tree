from rest_framework.routers import SimpleRouter
from .views import FamilyViewSet
router = SimpleRouter()
router.register("", FamilyViewSet, basename="family")
