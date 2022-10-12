from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from khayyam import JalaliDatetime

from Account.models import Account, BasketLines
from django.contrib.auth.decorators import login_required, user_passes_test
from MovieCrawl.models import Movie
from django.views.decorators.http import require_POST


def parser(request, moviename):
    film = Movie.objects.all().get(name=moviename)
    return HttpResponse(f"{film}")


def printer(request):
    # context = dict()
    # context['movie'] = Movie.objects.all()
    return render(request, template_name='movies.html')


@require_POST
def add_to_basket(request):
    # TODO:Check if user has Account_id in Cookie
    # TODO:Create and Design If Doesnt
    # TODO:Check If User Is Authenticated
    # TODO:Get Product From Submitted Form
    # TODO:Add Product To The Product Basketline
    # TODO:Return To The Next URL
    response = HttpResponseRedirect(request.POST.get('next', '/'))

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

    movie_id = request.POST.get('Movie_order', None)
    if movie_id is not None:
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            raise Http404
        else:
            account.add(movie)
    return response


def search(request, movie):
    return render(request, )