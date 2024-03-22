from django.db.models import Sum, Count
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.permissions import IsAdminOrReadOnly
from api.viewsets import CreateOrReadModelViewSet
from .models import Event, Collect
from .tasks import send_email_task
from .serializers import EventSerializer, PaymentSerializer, CollectSerializer

"""
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExNDQyNDM5LCJpYXQiOjE3MTEwMTA0MzksImp0aSI6Ijk2YWQ1MmM4Y2E0YjRkOTNhYWVjNDM1YjJmYWIxYzk1IiwidXNlcl9pZCI6MX0.4oAqVEdDr64GzaWjpX4PjI9lgfzP_pXoZRamWidv1tY
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExNTMxNTE2LCJpYXQiOjE3MTEwOTk1MTYsImp0aSI6IjhhZGYyZjY5NGU0NjQwMzQ4ZjkzZTg5YjNlZWRlOWMyIiwidXNlcl9pZCI6MX0.Q2UBlfiHh477PB8I336tPUaKRtaPLgHDp6E7dgrCu0o
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExNTMyODUwLCJpYXQiOjE3MTExMDA4NTAsImp0aSI6IjFjMDRmY2MzOTMxMTQ3NjdiMDJhMzYwNDY5ZThlZDYzIiwidXNlcl9pZCI6Mn0.KQMYHwIKfmQ9tNmliDnEZLj3cuGNGJvSpoxfgOzz8Bw
"""


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAdminOrReadOnly,)


class PaymentViewSet(CreateOrReadModelViewSet):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        # serializer.save(author_id=1, collect_id=self.kwargs['collect_id'])
        send_email_task.delay(self.request.user.email)
        serializer.save(author=self.request.user, collect_id=self.kwargs['collect_id'])

    def get_queryset(self):
        return self.get_collect_obj().payments.all()

    def get_collect_obj(self):
        return get_object_or_404(Collect, pk=self.kwargs['collect_id'])


class CollectViewSet(viewsets.ModelViewSet):
    serializer_class = CollectSerializer

    def perform_create(self, serializer):
        # serializer.save(author_id=1)
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Collect.objects.prefetch_related('payments').annotate(
            current_amount=Sum('payments__amount'), donation_total_counts=Count('payments')
        )
