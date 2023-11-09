from django.shortcuts import render
from rest_framework import viewsets
from .models import Journal
from .serializers import JournalSerializer

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    def get_object(self):
        # This method is used to retrieve the specific journal object
        # Override if necessary to handle lookup differently
        return super().get_object()