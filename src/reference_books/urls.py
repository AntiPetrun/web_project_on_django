from django.urls import path
from .views import by_genre

urlpatterns = [
    path('<int:genre_id>/', by_genre, name='by_genre'),
]
