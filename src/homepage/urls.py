from django.urls import path
from .views import index, by_genre, by_author

urlpatterns = [
    path('', index, name='index'),
    path('author/<int:author_id>/', by_author, name='by_author'),
    path('genre/<int:genre_id>/', by_genre, name='by_genre'),


]
