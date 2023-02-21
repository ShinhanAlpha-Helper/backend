from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Note
from .serializers import (
    NoteSerializer,
    NoteCreateSerializer,
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import datetime
from django.db.models import Sum

# Create your views here.

class NoteView (
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return NoteCreateSerializer
        return NoteSerializer

    def get_queryset(self):
        member = self.request.user.id
        return Note.objects.filter(member_id=member)

    def get (self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)    

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
    

class NoteTodayRankView (APIView):

    def get (self, request, *args, **kwargs):
        now = datetime.datetime.now()
        now_date = now.strftime('%Y-%m-%d')
        queryset = Note.objects.filter(tstamp__contains=now_date) \
                .values('title', 'count').order_by('title') \
                .annotate(total=Sum('count')).order_by('-total')[:3]
        
        print(queryset)

        ret = []
        for q in queryset:
            ret.append({
                'title': q['title'],
                'total': q['total'],
            })

        return Response(ret, status=status.HTTP_201_CREATED)

class NoteWeeklyRankView (APIView):

    def get (self, request, *args, **kwargs):
        startdate = request.query_params['startdate'] + " 00:00:00"
        lastdate = request.query_params['lastdate'] + " 23:59:59"
        
        start_time_obj = datetime.datetime.strptime(startdate, '%Y-%m-%d %H:%M:%S')
        last_time_obj = datetime.datetime.strptime(lastdate, '%Y-%m-%d %H:%M:%S')

        queryset = Note.objects.filter(tstamp__range=[start_time_obj, last_time_obj]) \
                .values('title', 'count').order_by('title') \
                .annotate(total=Sum('count')).order_by('-total')
        
        print(queryset)

        ret = []
        for q in queryset:
            ret.append({
                'title': q['title'],
                'total': q['total'],
            })

        return Response(ret, status=status.HTTP_201_CREATED)
