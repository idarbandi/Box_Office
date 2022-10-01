from django.shortcuts import render
from django.http import HttpResponse


def printer(request):
    return HttpResponse('movie crawled')