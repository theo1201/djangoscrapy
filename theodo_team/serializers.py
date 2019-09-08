
from theodo_team.models import TheodoTeam

from rest_framework import serializers

class TheodoTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheodoTeam
        fields = ['id', 'author', 'text']
    