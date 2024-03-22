from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

app_name = 'api'

v1_urlpatterns = [
    path('', include(router.urls)),
    path('', include('group_incomes.urls')),
]

urlpatterns = [
    path('v1/', include(v1_urlpatterns)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
