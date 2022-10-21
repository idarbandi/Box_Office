from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View

from Account.models import Account, BasketLines
from django.contrib.auth.decorators import login_required, user_passes_test
from MovieCrawl.models import Movie
from django.views.decorators.http import require_POST
from MovieCrawl.forms import AddToBasketForm


class main(View):
    template_name = 'movies.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


def parser(request, moviename):
    film = dict()
    film['search'] = Movie.objects.all().get(name=moviename)
    film['form'] = AddToBasketForm({"movie": film['search'].id, "quantity": 1})
    return render(request, 'movie.html', film)


@require_POST
def add_to_basket(request):
    response = HttpResponseRedirect(request.POST.get('next', 'dargah'))

    account = Account.account_validate(request.POST.get('account_id', None))
    if account is None:
        raise Http404

    response.set_cookie('account_id', account.id)

    if not account.user_validate(request.user):
        raise Http404

    form = AddToBasketForm(request.POST)
    if form.is_valid():
        form.save(account)

    return response


def search(request):
    movie_name = request.GET.get('box', None)
    if movie_name is not None:
        film = Movie.objects.filter(name__icontains=movie_name)
    return render(request, 'search.html', {"film": film})


def PayGateway(request):
    return HttpResponse("dargah_Pardakht")
