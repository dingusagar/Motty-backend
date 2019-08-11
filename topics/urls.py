from rest_framework.routers import DefaultRouter
from topics.views import TopicViewSet, CelebrityViewSet

router = DefaultRouter()
router.register(r'topic', TopicViewSet, basename='topic')
router.register(r'celebrity', CelebrityViewSet, basename='celebrity')

urlpatterns = router.urls
