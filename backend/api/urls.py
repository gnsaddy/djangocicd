from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', include('api.user_auth.urls')),
    path('course/', include('api.course.urls')),
    path('dashboard/', include('api.dashboard.urls')),
    path('demo/', include('api.demo.urls')),
    path('testimonial/', include('api.testimonial.urls')),
    path('', views.Home, name="api_home"),
]
