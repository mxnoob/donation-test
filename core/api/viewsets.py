from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CreateOrReadModelViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet
):
    pass
