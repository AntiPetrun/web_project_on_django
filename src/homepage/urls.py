from django.urls import path
from .views import by_genre, by_author, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('author/<int:author_id>/', by_author, name='by_author'),
    path('genre/<int:genre_id>/', by_genre, name='by_genre'),
]
