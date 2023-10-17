from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (EmailVerificationView, UserLoginView,
                         UserRegistrationView, logout, profile)

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('registration/', UserRegistrationView.as_view(), name = 'register'),
    path('profile/', profile, name = 'profile'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name = 'email_verification'),
    ]
