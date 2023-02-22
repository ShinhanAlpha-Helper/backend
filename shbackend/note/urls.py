from django.urls import path
from . import views

urlpatterns = [
    path("", views.NoteView.as_view()),
    path("/detail", views.NoteDetailView.as_view()),
    path("/rank/today", views.NoteTodayRankView.as_view()),
    path("/rank/weekly", views.NoteWeeklyRankView.as_view()),
    path("/bookmark", views.BookmarkCreateView.as_view()),
    path("/bookmark/view", views.BookmarkView.as_view()),
]