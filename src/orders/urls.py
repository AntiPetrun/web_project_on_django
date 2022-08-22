from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart', views.AddToCart.as_view(), name="add-to-cart"),
    path('delete-from-cart/<int:pk>/', views.DeleteFromCart.as_view(), name="delete-from-cart"),
    path('update-cart/', views.UpdateCart.as_view(), name="update-cart"),
]

urlpatterns += [
    path('all_orders', views.AllOrderListView.as_view(), name='all_orders'),
    path('user_orders', views.UserOrderListView.as_view(), name='user_orders'),
    path('order-detail', views.OrderDetailView.as_view(), name='order-detail'),
]
