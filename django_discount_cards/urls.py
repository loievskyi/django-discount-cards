from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("discount-cards/", include("discount_cards.urls")),
    path("api/v1/", include("core.urls"), name="api"),
    path("", RedirectView.as_view(url="discount-cards/")),
]
