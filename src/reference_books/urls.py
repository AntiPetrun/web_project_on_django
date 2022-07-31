from django.urls import path
from .views import AuthorDetailView, AuthorListView

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/detail', AuthorDetailView.as_view(), name='author-detail'),
]
