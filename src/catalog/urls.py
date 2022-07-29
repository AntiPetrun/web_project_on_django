from django.urls import path
from .views import BookCreateView, BookSeriaCreateView

urlpatterns = [
    path('add-book/', BookCreateView.as_view(), name='add-book'),
    path('add-book-seria/', BookSeriaCreateView.as_view(), name='add-book-seria'),
]
