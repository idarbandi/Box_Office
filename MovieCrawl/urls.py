from django.conf.urls.static import static
from django.urls import path
from MovieCrawl.views import printer, director, download, welcome, parser


urlpatterns = [
                  path('movie/main', printer),
                  path('movie/detail/<str:moviename>', parser, name='parser_name'),
                  path('movie/director/<slug:dir_nm>', director),
                  path('movie/distributer/search/', download),
                  path('movie/login/', welcome)
              ]
