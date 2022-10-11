from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from MovieCrawl.models import Movie
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from MovieCrawl.models import Movie
from django.views.decorators.http import require_POST


def parser(request, moviename):
    film = Movie.objects.all().get(name=moviename)
    return HttpResponse(f"{film}")


def printer(request):
    # context = dict()
    # context['movie'] = Movie.objects.all()
    return render(request, template_name='movies.html')


@login_required
@require_POST
@user_passes_test(lambda fun: fun.is_staff)
def add_to_basket(request):
    #TODO:Check if user has basket_id in Cookie
    #TODO:Create and Design If Doesnt
    #TODO:Get Product From Submitted Form
    return HttpResponseRedirect(redirect_to='/redirect')
