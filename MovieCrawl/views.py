from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from Account.models import Account, BasketLines
from django.contrib.auth.decorators import login_required, user_passes_test
from MovieCrawl.models import Movie
from django.views.decorators.http import require_POST
from MovieCrawl.forms import AddToBasketForm


def parser(request, moviename):
    film = dict()
    film['search'] = Movie.objects.all().get(name=moviename)
    film['form'] = AddToBasketForm({"movie": film['search'].id, "quantity": 1})
    return render(request, 'movie.html', film)


def printer(request):
    return render(request, template_name='movies.html')


@require_POST
def add_to_basket(request):
    # TODO:Check if user has Account_id in Cookie
    # TODO:Create and Design If Doesnt
    # TODO:Check If User Is Authenticated
    # TODO:Get Product From Submitted Form
    # TODO:Add Product To The Product Basketline
    # TODO:Return To The Next URL
    response = HttpResponseRedirect(request.POST.get('next', 'dargah'))

    account_id = request.POST.get('account_id', None)
    if account_id is None:
        account = Account.objects.create()
        response.set_cookie('account_id', account.id)
    else:
        try:
            account = Account.objects.get(pk=account_id)
        except Account.DoesNotExist:
            raise Http404

    if request.user.is_authenticated:
        if account.user is not None and account.user != request.user:
            raise Http404
    account.user = request.user
    account.save()

    form = AddToBasketForm(request.POST)
    if form.is_valid():
        form.save(account)
    return response


def search(request):
    movie_name = request.POST.get('box', None)
    if movie_name is not None:
        film = Movie.objects.all().filter(name__icontains=movie_name)
    return render(request, template_name='search.html', context=film)


def PayGateway(request):
    return HttpResponse("dargah_Pardakht")
