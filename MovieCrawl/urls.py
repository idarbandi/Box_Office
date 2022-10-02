from django.urls import path
from MovieCrawl.views import printer, director

urlpatterns = [
    path('movie/<str:moviename>', printer),
    path('movie/director/<slug:dir_nm>', director)
]
