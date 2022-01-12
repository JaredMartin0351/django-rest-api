from abc import abstractstaticmethod
from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songfields = ['id', 'title', 'artist', 'album', 'genre', 'release_date']