from django.shortcuts import render
from django.http import HttpResponse

from MovieCrawl.models import Movie, DirMovie


def printer(request, moviename):
    try:
        movie = Movie.objects.filter(name=moviename)
        return HttpResponse(f"{movie}")
    except Movie.DoesNotExist:
        return HttpResponse("Movie not Found")


def director(request, dir_nm):
    return HttpResponse(f"{dir_nm}")