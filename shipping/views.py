from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic import CreateView, ListView, FormView

from shipping.forms import shippingForm
from shipping.models import shipping


class address_create(FormView):
    model = shipping
    form_class = shippingForm
    template_name = 'shipping.html'
    success_url = reverse_lazy('list')

    @method_decorator(login_required, require_http_methods(request_method_list=['GET', 'POST']))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)


class address_list(ListView):
    template_name = 'address_list.html'
    model = shipping
    queryset = shipping.objects.all()
    context_object_name = 'form'

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(user=self.request.user)