from django.contrib import admin
from .models import Note, Bookmark

# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    pass