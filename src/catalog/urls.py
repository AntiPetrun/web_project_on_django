from django.urls import path
from .views import BookCreateView, BookSeriaCreateView, BookDetailView, BookDeleteView, BookListView, BookUpdateView, BookSeriaDetailView, BookSeriaListView, BookSeriaUpdateView, BookSeriaDeleteView

urlpatterns = [
    path('edit-book/<int:pk>/update', BookUpdateView.as_view(), name='edit-book'),
    path('books/', BookListView.as_view(), name='books'),
    path('delete-book/<int:pk>/delete', BookDeleteView.as_view(), name='delete-book'),
    path('book/<int:pk>/detail', BookDetailView.as_view(), name='book-detail'),
    path('add-book/', BookCreateView.as_view(), name='add-book'),
]

urlpatterns += [
    path('delete-book-seria/<int:pk>/delete', BookSeriaDeleteView.as_view(), name='delete-book-seria'),
    path('edit-book-seria/<int:pk>/update', BookSeriaUpdateView.as_view(), name='edit-book-seria'),
    path('book-series/', BookSeriaListView.as_view(), name='book-series'),
    path('book-seria/<int:pk>/detail', BookSeriaDetailView.as_view(), name='book-seria-detail'),
    path('add-book-seria/', BookSeriaCreateView.as_view(), name='add-book-seria'),
]
