from django.urls import path

# importing views from views..py
from .views import geeks_view
from .views import geeks_2

urlpatterns = [
    path('', geeks_view),
    path('test/', geeks_2),
]
