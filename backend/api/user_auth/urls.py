from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import MyTokenObtainPairView, LogoutAllView
from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'student', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.Home.as_view(), name="home"),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('logout_all/', LogoutAllView.as_view(), name='logout_all'),
    path("tokenrefresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path('tokenverify/', TokenVerifyView.as_view(), name='token_verify'),

]
