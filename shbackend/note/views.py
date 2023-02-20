from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Note
from .serializers import (
    NoteSerializer,
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class NoteView (
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [IsAuthenticated]

    serializer_class = NoteSerializer

    def get_queryset(self):
        member = self.request.user.id
        return Note.objects.filter(member_id=member)

    def get (self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def delete (self, request, *args, **kwargs):
        noteid = request.data.get('id')
        memberid = request.user.id
        note = Note.objects.filter(id=noteid, member_id=memberid)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NoteDetailView (
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [IsAuthenticated]

    serializer_class = NoteSerializer

    def get_queryset(self):
        member = self.request.user.id
        notetitle = self.request.query_params['title']
        return Note.objects.filter(member_id=member, title=notetitle)

    def get (self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
