from rest_framework import routers
from .views import PartViewSet


router = routers.DefaultRouter()
router.register(r'parts', PartViewSet)
urlpatterns = router.urls
