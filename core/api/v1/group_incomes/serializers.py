from rest_framework import serializers

from group_incomes.models import Collect, Event, Payment


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title',)


class PaymentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='email', read_only=True)

    class Meta:
        model = Payment
        fields = ('amount', 'message', 'author', 'created_at')
        read_only_fields = ('author', 'created_at')


class CollectPresentationSerializer(serializers.ModelSerializer):
    current_amount = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    donation_total_counts = serializers.IntegerField(read_only=True)
    author = serializers.SlugRelatedField(slug_field='email', read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Collect
        fields = '__all__'


class CollectDetailSerializer(CollectPresentationSerializer):
    payments = PaymentSerializer(many=True, read_only=True)
