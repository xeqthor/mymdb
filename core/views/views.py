from django.views.generic import (
    ListView,
    DetailView,
)
from core.models import Movie, Person


class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    model = Movie


class PersonDetail(DetailView):
    queryset = Person.related_objects.all_with_prefetch_movies()


class MovieDetail(DetailView):
    queryset = (
        Movie.related_objects.all_with_related_persons())
