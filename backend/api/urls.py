from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', include('api.user_auth.urls')),
    path('', views.Home, name="api_home"),
]
