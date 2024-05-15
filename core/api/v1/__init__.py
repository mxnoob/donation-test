from django.urls import include, path

from .group_incomes import urls as group_incomes_urls

urlpatterns = [
    path('', include(group_incomes_urls)),
]
