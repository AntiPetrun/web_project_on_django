from django.urls import path
from .views import BookCreateView

urlpatterns = [
    path('add/', BookCreateView.as_view(), name='add'),
]
