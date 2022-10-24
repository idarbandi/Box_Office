from django.urls import path

from financial.views import PayRequest, PayConfirm

urlpatterns = [
    path('charge/', PayRequest.as_view(), name='pay'),
    path('verify/', PayConfirm.as_view()),
    # path('pay/<str:invoice_number>/<str:gateway_code>/')
]
