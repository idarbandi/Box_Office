from django.urls import path

from financial.views import Pay, PostGateway, verify

urlpatterns = [
    path('pay/<str:invoice_number>', Pay.as_view(), name='PurchaseDirect'),
    path('pay/<str:invoice_number>/<str:gateway_code>', PostGateway.as_view(), name='PostGateWay'),
    path('verify/', verify.as_view())
]
