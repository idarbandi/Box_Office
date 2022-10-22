from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, FormView

from Account.models import Account, BasketLines
from django.contrib.auth.decorators import login_required, user_passes_test
from MovieCrawl.models import Movie
from django.views.decorators.http import require_POST
from MovieCrawl.forms import AddToBasketForm


class main(View):
    template_name = 'movies.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class movie(DetailView, FormView):
    model = Movie
    template_name = 'movie.html'
    queryset = Movie.objects.all()
    form_class = AddToBasketForm
    initial = {"movie": None, "quantity": 1}

    def get(self, request, *args, **kwargs):
        self.initial['movie'] = kwargs.get('pk')
        return super().get(request, *args, **kwargs)
class Shop(FormView):
    success_url = 'dargah'
    form_class = AddToBasketForm
    initial = None

    @method_decorator(require_POST, login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        account = Account.account_validate(request.POST.get('account_id', None))
        if account is None:
            raise Http404
        self.request.session['account_id'] = account.id
        if not account.user_validate(request.user):
            raise Http404
        self.initial = request.POST

        return super().post(request, *args, **kwargs)

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
