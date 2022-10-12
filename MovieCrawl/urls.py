from django.conf.urls.static import static
from django.urls import path
from MovieCrawl.views import printer, parser, add_to_basket, searchbox


urlpatterns = [
                  path('movie/main', printer),
                  path('movie/detail/<str:moviename>', parser, name='parser_name'),
                  path('movie/search/<str:moviename>', searchbox, name='searchbox'),
                  path('movie/account/addToBasket', add_to_basket, name='add')
              ]
