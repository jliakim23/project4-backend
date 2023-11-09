from .models import Journal
from rest_framework import serializers
from django.contrib.auth.models import User

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'mood', 'activities', 'photo', 'date']