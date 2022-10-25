from django.urls import path, include
from package.views import BuyPackage

urlpatterns = [
    path('buy/', BuyPackage.as_view(), name='BuyPackage'),
    path('purchase/', include('purchase.urls'))
]
