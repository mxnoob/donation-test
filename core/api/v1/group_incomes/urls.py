from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CollectViewSet, EventViewSet, PaymentViewSet

app_name = 'group_incomes'

router = DefaultRouter()
router.register('events', EventViewSet, basename='events')
router.register('collects', CollectViewSet, basename='collects')
router.register(
    r'collects/(?P<collect_id>\d+)/payments',
    PaymentViewSet,
    basename='payments',
)


urlpatterns = [path('', include(router.urls))]
