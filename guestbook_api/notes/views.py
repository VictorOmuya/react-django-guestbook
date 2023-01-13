from django.shortcuts import render
from .models import Notes
from .serializers import NoteSerializer
from rest_framework import viewsets
# Create your views here.

class NoteViewSets(viewsets.ModelViewSet):
    serializer_class= NoteSerializer
    queryset = Notes.objects.all()