from django.shortcuts import render
from django.http import HttpResponse
from MovieCrawl.models import Movie
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from MovieCrawl.models import Movie, DirMovie


def parser(request, moviename):
    film = Movie.objects.all().get(name=moviename)
    return HttpResponse(f"{film}")


def printer(request):
    # context = dict()
    # context['movie'] = Movie.objects.all()
    return render(request, template_name='movies.html')


def director(request, dir_nm):
    return HttpResponse(f"{dir_nm}")


def download(request):
    query = request.GET.get('q')
    response = Movie.objects.all().filter(name__icontains=query).first()
    return HttpResponse(f"{response}")


@login_required
@user_passes_test(lambda fun: fun.is_staff)
def welcome(request):
    return HttpResponse(f"hello {request.user.username}")
