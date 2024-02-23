from rest_framework import serializers
from .models import Note, NoteVersion

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        # fields = '__all__'
        fields = ['id', 'title', 'content']

class NoteVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteVersion
        fields = '__all__'

