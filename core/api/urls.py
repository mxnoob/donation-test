from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('v1/', include('api.v1')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
