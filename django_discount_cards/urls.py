from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("discount-cards/", include("discount_cards.urls")),
    path("api/v1/", include("core.urls")),
]
