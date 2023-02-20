from django.urls import path
from . import views

urlpatterns = [
    path("/domestic", views.DomesticNewsView.as_view()),
    path("/overseas", views.OverseasNewsView.as_view()),
]