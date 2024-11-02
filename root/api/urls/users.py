from django.urls import path
from ..views.users import (
    UserRegisterAPIView,
    UserListAPIView, 
    UserLoginAPIView,
    UserPasswordResetAPIView,
    UserProfileAPIView,
    EditProfileAPIView,
    UserLogoutAPIView
)

urlpatterns = [
    path('api/user/register/', UserRegisterAPIView.as_view(), name = 'api-user-register'),
    path('api/user/list/', UserListAPIView.as_view(), name = 'api-user-list'),
    path('api/user/login/', UserLoginAPIView.as_view(), name = 'api-user-login'),
    path('api/user/password/reset/<int:id>/', UserPasswordResetAPIView.as_view(), name = 'api-user-password-reset'),
    path('api/user/profile/', UserProfileAPIView.as_view(), name = 'api-user-profile'),
    path('api/user/profile/edit/', EditProfileAPIView.as_view(), name = 'api-user-profile-edit'),
    path('api/user/logout/', UserLogoutAPIView.as_view(), name = 'api-user-logout')
]
