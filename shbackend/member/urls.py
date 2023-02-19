from django.urls import path
from . import views

urlpatterns = [
    path("/register", views.MemberRegisterView.as_view()),
    path("/password", views.MemberChangePasswordView.as_view()),
]