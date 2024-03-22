from django.db.models import Sum, Count
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.permissions import IsAdminOrReadOnly
from api.viewsets import CreateOrReadModelViewSet
from .models import Event, Collect
from .serializers import EventSerializer, PaymentSerializer, CollectSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAdminOrReadOnly,)


class PaymentViewSet(CreateOrReadModelViewSet):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, collect_id=self.kwargs['collect_id'])

    def get_queryset(self):
        return self.get_collect_obj().payments.all()

    def get_collect_obj(self):
        return get_object_or_404(Collect, pk=self.kwargs['collect_id'])


class CollectViewSet(viewsets.ModelViewSet):
    serializer_class = CollectSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Collect.objects.prefetch_related('payments').annotate(
            current_amount=Sum('payments__amount'), donation_total_counts=Count('payments')
        )
