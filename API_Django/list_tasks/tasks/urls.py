from rest_framework.routers import DefaultRouter
from .viewsets import TasksViewSet

router = DefaultRouter()
router.register('',TasksViewSet)

urlpatterns =  router.urls