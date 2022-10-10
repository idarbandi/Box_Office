from MovieCrawl.models import Movie
from django import template

register = template.Library()


@register.simple_tag
def feeder():
    return Movie.objects.all()


def actors():
    return Movie.actor_id.all()