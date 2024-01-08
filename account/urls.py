from django.urls import path,include
# from .views import UserRegistrationView,UserLoginView,UserProfileView,UserChangePassword,SendPasswordResetEmailView,UserPasswordResetView
from account.views import *
urlpatterns = [
    path('register/',UserRegistrationView.as_view()),
    path('login/',UserLoginView.as_view()),
    path('profile/',UserProfileView.as_view()),
    path('changepassword/',UserChangePassword.as_view()),
    path('send-reset-password-email/',SendPasswordResetView.as_view()),
    # path('reset-password/<uid>/<token>',UserPasswordResetView.as_view(),name='reset-password'),
    path("reset-password/<uid>/<token>", UserPasswordResetView.as_view(), name="resetpassword"),
    path('updateProfile/<int:pk>',UserProfileUpdate.as_view()),
    # path('')
] 
