from django.urls import path, include

from .group_incomes import urls as group_incomes_urls

urlpatterns = [
    path('', include(group_incomes_urls)),
]
