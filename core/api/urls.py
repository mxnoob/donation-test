from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'api'

urlpatterns = [
    path('v1/', include('api.v1')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
