from rest_framework import viewsets
from rest_framework import permissions

from sites.models import Afocha, Deceased
from rest_api.serializers import AfochaSerializer, DeceasedSerializer

class DeceasedViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited.
    '''
    queryset = Deceased.objects.all().order_by('efname')
    serializer_class = DeceasedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AfochaViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited.
    '''
    queryset = Afocha.objects.all().order_by('name')
    serializer_class = AfochaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
