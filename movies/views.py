from django.shortcuts import render
from django.views.generic import ListView, DetailView

from movies.models import Movie


class MovieDetailView(DetailView):
    """Indvidual movie detailed view."""

    model = Movie
    template_name = "movie.html"
    context_object_name = "movie"