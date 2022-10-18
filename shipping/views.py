from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET

from shipping.forms import shippingForm, listForm
from shipping.models import shipping


@login_required
@require_http_methods(request_method_list=['GET', 'POST'])
def address_create(request):
    if request.method == "POST":
        form = shippingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        form = shippingForm()
    return render(request, 'shipping.html', {"form": form})


@login_required
@require_GET
def address_list(request):
    form = shipping.objects.filter(user=request.user)
    return render(request, 'address_list.html', {"form": form})
