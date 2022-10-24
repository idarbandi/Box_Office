from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, FormView, RedirectView, ListView

from Account.models import Account
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


class Shop(RedirectView):
    pattern_name = 'pay'

    @method_decorator(require_POST)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(login_required())
    def post(self, request, *args, **kwargs):
        account = Account.account_validate(request.POST.get('account_id', None))
        if account is None:
            raise Http404
        self.request.session['account_id'] = account.id
        if not account.user_validate(request.user):
            raise Http404
        form = AddToBasketForm(request.POST)
        if form.is_valid():
            form.save(account)
            return super().post(request)


class Search(ListView):
    model = Movie
    template_name = 'search.html'
    context_object_name = 'Search'

    def get_queryset(self):
        qs = super().get_queryset()
        movie_name = self.request.GET.get('box', None)
        print(self.request.GET.get('box', None))
        return qs.filter(name__icontains=movie_name)



def PayGateway(request):
    return HttpResponse("dargah_Pardakht")
