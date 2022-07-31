from django.urls import path
from .views import BookCreateView, BookSeriaCreateView, BookDetailView, BookDeleteView, BookListView, BookUpdateView

urlpatterns = [
    path('edit-book/<int:pk>/update', BookUpdateView.as_view(), name='edit-book'),
    path('books/', BookListView.as_view(), name='books'),
    path('delete-book/<int:pk>/delete', BookDeleteView.as_view(), name='delete-book'),
    path('book/<int:pk>/detail', BookDetailView.as_view(), name='book-detail'),
    path('add-book/', BookCreateView.as_view(), name='add-book'),
]

urlpatterns += [
    path('add-seria/', BookSeriaCreateView.as_view(), name='add-seria'),
]