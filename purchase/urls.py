from django.urls import path

from purchase.views import Purchase_pkg

urlpatterns = [
    path('pack/<int:package_id>', Purchase_pkg.as_view(), name='purchase_pkg'),
]