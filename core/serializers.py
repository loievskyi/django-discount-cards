from django.contrib.auth.models import User
from rest_framework import serializers

from discount_cards.models import DiscountCard, Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"


class DiscountCardSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username",
                                        queryset=User.objects.all())

    class Meta:
        model = DiscountCard
        fields = "__all__"


class DiscountCardRetrieveSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username",
                                        queryset=User.objects.all())
    purchases = PurchaseSerializer(many=True, read_only=True)

    class Meta:
        model = DiscountCard
        fields = "__all__"
