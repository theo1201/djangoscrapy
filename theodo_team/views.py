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


def ScrapydData(request):
    from scrapyd_api import ScrapydAPI
    scrapyd = ScrapydAPI('http://localhost:6800')
    settings = {'DOWNLOAD_DELAY': 2}
    # 运行一个爬虫
    scrapyd.schedule('project_name', 'spider_name', settings=settings)
    print(scrapyd.list_projects())
