from django.urls import path
from .views import index, by_genre, ReferenceBookCreateView

urlpatterns = [
    path('add/', ReferenceBookCreateView.as_view(), name='add'),
    path('<int:genre_id>/', by_genre, name='by_genre'),
    path('', index, name='index'),
]
