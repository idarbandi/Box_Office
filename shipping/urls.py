from django.urls import path
from shipping.views import address_list, address_create


urlpatterns = [
    path('address/create', address_create, name='create'),
    path('address/list', address_list, name='list')

]