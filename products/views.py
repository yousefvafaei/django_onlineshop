from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404, reverse
from django.http import HttpResponse
from django.utils.translation import gettext as _

from .models import Product, Comment
from .forms import CommentForm


def test_translation(request):
    result = _('Hello')
    return HttpResponse(result)


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        # ta khat zir fagat form zakhire mishe va fagat overwrite kardim
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        return super().form_valid(form)