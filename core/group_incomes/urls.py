from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EventViewSet, PaymentViewSet, CollectViewSet

app_name = 'group_incomes'
router_v1 = DefaultRouter()
router_v1.register('events', EventViewSet, basename='events')
router_v1.register('collects', CollectViewSet, basename='collects')
router_v1.register(r'collects/(?P<collect_id>\d+)/payments', PaymentViewSet, basename='payments')


urlpatterns = [path('', include(router_v1.urls))]
