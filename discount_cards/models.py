from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class DiscountCard(models.Model):
    seria = models.CharField(_("discount_card.seria"), max_length=2)
    number = models.PositiveIntegerField(_("discount_card.number"))
    release_date = models.DateTimeField(_("discount_card.release_date"))
    end_date = models.DateTimeField(_("discount_card.end_date"))
    last_use = models.DateTimeField(_("discount_card.last_use"))
    sum = models.DecimalField(_("discount_card.sum"), max_digits=19,
                              decimal_places=4)
    status = models.BooleanField(_("discount_card.status"))
    user = models.ForeignKey(User, on_delete=models.PROTECT,
                             verbose_name=_("discount_card.user"))

    def __str__(self):
        return f"{self.seria} {self.number}"

    class Meta:
        verbose_name = _("discount_card")
        verbose_name_plural = _("discount_cards")


class Purchase(models.Model):
    discount_card = models.ForeignKey(DiscountCard, on_delete=models.CASCADE,
                                      verbose_name=_("purchase.purchase"))
    date = models.DateTimeField(_("purchase.date"), auto_now=True)
    purchase_amount = models.DecimalField(_("purchase.purchase_amount"),
                                          max_digits=19, decimal_places=4)

    def __str__(self):
        return f"{self.discount_card} - {self.date} - {self.purchase_amount}"

    class Meta:
        verbose_name = _("purchase")
        verbose_name_plural = _("purchases")
