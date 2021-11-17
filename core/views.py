from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from discount_cards.models import DiscountCard
from .serializers import DiscountCardSerializer, DiscountCardRetrieveSerializer


class DiscountCardViewSet(ModelViewSet):
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,
                       DjangoFilterBackend)
    search_fields = ("seria", "number", "status", "end_date")
    ordering_fields = ("-release_date",)
    filterset_fields = "__all__"
    serializer_class = DiscountCardSerializer

    def get_queryset(self):
        return DiscountCard.objects.select_related("user")

    def retrieve(self, request, pk, *args, **kwargs):
        queryset = DiscountCard.objects.all()
        discount_card = get_object_or_404(queryset, pk=pk)
        serializer = DiscountCardRetrieveSerializer(discount_card)
        return Response(serializer.data)
