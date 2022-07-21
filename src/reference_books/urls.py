from django.urls import path
from .views import index, by_genre

urlpatterns = [
    path('<int:genre_id>/', by_genre),
    path('', index),
]
