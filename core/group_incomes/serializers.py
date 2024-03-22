from rest_framework import serializers

from .models import Event, Payment, Collect
from .services import success_created_payment_email, success_created_collect_email


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title',)


class PaymentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='email', read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Payment
        fields = ('amount', 'message', 'author', 'created_at')
        read_only_fields = ('author', 'created_at')

    def create(self, validated_data):
        instance = super().create(validated_data)
        if instance:
            success_created_payment_email(instance.author.email)
        return instance


class CollectPresentationSerializer(serializers.ModelSerializer):
    current_amount = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    donation_total_counts = serializers.IntegerField(read_only=True)
    author = serializers.SlugRelatedField(slug_field='email', read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Collect
        fields = '__all__'


class CollectDetailSerializer(CollectPresentationSerializer):
    payments = PaymentSerializer(many=True, read_only=True)


class CollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collect
        fields = '__all__'
        read_only_fields = ('author',)

    def create(self, validated_data):
        instance = super().create(validated_data)
        if instance:
            success_created_collect_email(instance.author.email)
        return instance

    def to_representation(self, instance):
        if self.context['view'].action == 'retrieve':
            return CollectDetailSerializer(instance).data
        return CollectPresentationSerializer(instance).data
