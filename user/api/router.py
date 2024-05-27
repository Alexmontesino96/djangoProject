from rest_framework.routers import DefaultRouter
from user.api.view import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from user.api.view import UserView

urlpatterns = [
    path('user/register/', RegisterView.as_view(),),
    path('user/login/', TokenObtainPairView.as_view(),),
    path('user/refresh/', TokenRefreshView.as_view(),),
    path('user/me/', UserView.as_view(),),
]
