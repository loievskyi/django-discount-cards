from rest_framework import routers

from core import views


app_name = "core"


router = routers.SimpleRouter()
router.register(r"discount-cards", views.DiscountCardViewSet,
                basename="discount-card")

urlpatterns = router.urls
