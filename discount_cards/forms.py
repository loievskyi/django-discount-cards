from django.forms import ModelForm

from .models import DiscountCard, Purchase


class DiscountCardForm(ModelForm):
    class Meta:
        model = DiscountCard
        fields = "__all__"


class ReadOnlyDiscountCardForm(ModelForm):
    class Meta:
        model = DiscountCard
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["readonly"] = True


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"
