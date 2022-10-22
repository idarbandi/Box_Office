from django.conf.urls.static import static
from django.urls import path
from MovieCrawl.views import movie, add_to_basket, search, PayGateway, main, Shop

urlpatterns = [
                  path('movie/main', main.as_view()),
                  path('movie/<int:pk>', movie.as_view(), name='movie'),
                  path('movie/search/', search, name='searchbox'),
                  path('movie/account/addToBasket', Shop.as_view(), name='add'),
                  path('movie/account/dargah', PayGateway, name='dargah')
              ]
