from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),            # home page
    path('stocks/', views.stock_list, name='stock_list'),  # stock list
]
