from django.core.cache import cache
from django.db.models import Sum, Count
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.permissions import IsAdminOrReadOnly
from api.viewsets import CreateOrReadModelViewSet
from group_incomes.models import Event, Collect
from .serializers import EventSerializer, PaymentSerializer, CollectPresentationSerializer, CollectDetailSerializer


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
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CollectDetailSerializer
        return CollectPresentationSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        collects = cache.get('collects')
        if collects is None:
            collects = (
                Collect.objects.prefetch_related('payments')
                .select_related('author')
                .annotate(current_amount=Sum('payments__amount'), donation_total_counts=Count('payments'))
            )
            cache.set('collects', collects, 60 * 15)
        return collects

    def get_object(self):
        cache_key = 'collect:%s' % self.kwargs['pk']
        obj = cache.get(cache_key)
        if obj is None:
            obj = super().get_object()
            cache.set(cache_key, obj, 60 * 15)
        return obj
