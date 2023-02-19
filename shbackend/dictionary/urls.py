from django.urls import path
from . import views

urlpatterns = [
    path("", views.DictionarySearchView.as_view()),
]