from django.shortcuts import render
from django.http import HttpResponse
from transactions.models import transaction


def trans(request):
    tr = transaction.calculate()
    return HttpResponse(f"{tr}")
