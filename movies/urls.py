from django.urls import path

from movies.views import MovieDetailView


urlpatterns = [
    path("<slug:slug>/", MovieDetailView.as_view(), name="movie_detail"),
]