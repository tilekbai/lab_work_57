from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.db.models import Q
from django.utils.http import urlencode
from django.urls import reverse_lazy

from shop.models import Product
from shop.forms import SearchForm, ProductForm
# Create your views here.


class MainpageView(ListView):
    template_name = "main.html"
    model = Product
    context_object_name = "products"
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()

        return super(MainpageView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_data:
            queryset = queryset.filter(
                Q(summary__icontains = self.search_data) |
                Q(description__icontains = self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data["search_value"]
        return None


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form

        if self.search_data:
            context["query"] = urlencode({"search_value": self.search_data})

        return context


class ProductView(DetailView):
    template_name = "product/product_view.html"
    model = Product


class Product_updateView(UpdateView):
    model = Product
    template_name = 'product/product_update.html'
    form_class = ProductForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product-view', kwargs={'pk': self.object.pk})
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)


class Product_deleteView(DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('product-list')


class Product_createView(CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product-view', kwargs={'pk': self.object.pk})