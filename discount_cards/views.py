from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import DiscountCard, Purchase
from .forms import ReadOnlyDiscountCardForm


class DiscountCardView(DetailView):
    model = DiscountCard
    template_name = "discount_cards/single.html"
    context_object_name = "discount_card"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card = kwargs["object"]
        purchases = Purchase.objects.filter(discount_card_id=card.id)
        card_form = ReadOnlyDiscountCardForm(instance=card)
        context["card"] = card
        context["purchases"] = purchases
        context["card_form"] = card_form
        return context


class DiscountCardListView(ListView):
    model = DiscountCard
    template_name = "discount_cards/discount_cards_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cards = self.get_queryset()
        page = self.request.GET.get("page")
        paginator = Paginator(cards, self.paginate_by)
        try:
            cards = paginator.page(page)
        except PageNotAnInteger:
            cards = paginator.page(1)
        except EmptyPage:
            cards = paginator.page(paginator.num_pages)
        context["cards"] = cards
        return context


class DiscountCardUpdateStatusView(UpdateView):
    model = DiscountCard
    fields = ["status"]
    template_name = "discount_cards/change_status.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse("discount_cards:edit_card", kwargs={"pk": self.object.pk})

    def get_absolute_url(self):
        return reverse("discount_cards:edit_card", kwargs={"pk": self.object.pk})
