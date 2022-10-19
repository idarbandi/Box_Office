from django.urls import path
from shipping.views import address_create, address_list


urlpatterns = [
    path('address/create', address_create.as_view(), name='create'),
    path('address/list', address_list.as_view(), name='list')

]