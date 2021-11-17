from django.urls import path
from django.views.generic.base import RedirectView

from .views import DiscountCardListView, DiscountCardView, DiscountCardUpdateStatusView


app_name = "discount_cards"


urlpatterns = [
    path("list/", DiscountCardListView.as_view(), name="card-list"),
    path("<int:pk>/", DiscountCardView.as_view(),
         name="card_detail"),
    path("edit/<int:pk>/", DiscountCardUpdateStatusView.as_view(),
         name="edit_card"),
    # path("delete/<int:pk>/", DiscountCardDeleteView.as_view(),
    #      name="delete_card"),
    path("", RedirectView.as_view(url="list/")),
]
