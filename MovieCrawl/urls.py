from django.conf.urls.static import static
from django.urls import path
from MovieCrawl.views import parser, add_to_basket, search, PayGateway, main

urlpatterns = [
                  path('movie/main', main.as_view()),
                  path('movie/detail/<str:moviename>', parser, name='parser_name'),
                  path('movie/search/', search, name='searchbox'),
                  path('movie/account/addToBasket', add_to_basket, name='add'),
                  path('movie/pay', PayGateway, name='dargah')
              ]
