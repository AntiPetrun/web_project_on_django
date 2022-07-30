from django.urls import path
from .views import BookCreateView, BookSeriaCreateView, BookDetailView, BookDeleteView

urlpatterns = [
    path("delete-book/<int:pk>", BookDeleteView.as_view(), name="delete-book"),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('add-book/', BookCreateView.as_view(), name='add-book'),
]

urlpatterns += [
    path('add-seria/', BookSeriaCreateView.as_view(), name='add-seria'),
]