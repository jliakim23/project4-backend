from django.shortcuts import render

# Create your views here.
from .models import Journal
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import JournalSerializer


class JournalViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Journal.objects.all()
    # The serializer class for serializing output
    serializer_class = JournalSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]