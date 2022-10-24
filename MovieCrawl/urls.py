from django.conf.urls.static import static
from django.urls import path, include
from MovieCrawl.views import movie, PayGateway, main, Shop, Search

urlpatterns = [
                  path('movie/main', main.as_view()),
                  path('movie/<int:pk>', movie.as_view(), name='movie'),
                  path('movie/search', Search.as_view(), name='searchbox'),
                  path('movie/account/addToBasket', Shop.as_view(), name='add'),
                  path('movie/account/financial/', include('financial.urls')),
                  path('movie/account/package', include('package.urls'))
              ]
