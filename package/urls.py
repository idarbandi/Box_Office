from django.urls import path
from package.views import BuyPackage

urlpatterns = [
    path('buy', BuyPackage.as_view(), name='BuyPackage')
]
