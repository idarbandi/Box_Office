from django.urls import path
from MovieCrawl.views import printer

urlpatterns = [
    path('movie/', printer)
]
