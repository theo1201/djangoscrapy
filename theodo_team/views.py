# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from theodo_team.models import TheodoTeam
from theodo_team.serializers import TheodoTeamSerializer

class TheodoTeamViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = TheodoTeam.objects.all()
    serializer_class = TheodoTeamSerializer