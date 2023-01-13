from .models import Notes
from rest_framework import serializers

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'