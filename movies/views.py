from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Movie

def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})


from django.shortcuts import render
from django.http import JsonResponse
from .models import Genre, Movie
from django.db.models import Count

def dashboard_page(request):
    return render(request, 'dashboard.html')

def dashboard_data(request):
    genre_stats = Genre.objects.annotate(count=Count('movie')).values('name', 'count')
    top_movies = Movie.objects.order_by('-rating')[:5].values('title', 'rating')

    return JsonResponse({
        'genres': list(genre_stats),
        'top_movies': list(top_movies),
    })


from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



