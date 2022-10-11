from django.conf.urls.static import static
from django.urls import path
from MovieCrawl.views import printer, parser, add_to_basket


urlpatterns = [
                  path('movie/main', printer),
                  path('movie/detail/<str:moviename>', parser, name='parser_name'),
                  path('movie/director/search/addToBasket', add_to_basket, name='add')
              ]
