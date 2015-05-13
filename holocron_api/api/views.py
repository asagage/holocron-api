from api.models import Source, Medium, Campaign, Content, Placement
from rest_framework import viewsets
from api.serializers import SourceSerializer, MediumSerializer, \
    CampaignSerializer, ContentSerializer, PlacementSerializer, \
    PlacementDetailsSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Campaigns to be viewed or edited.
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class MediumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Mediums to be viewed or edited.
    """
    queryset = Medium.objects.all()
    serializer_class = MediumSerializer


class SourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sources to be viewed or edited.
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class ContentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Content to be viewed or edited.
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class PlacementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Placements (with Foreign Keys)
    to be viewed or edited.
    """
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer


class PlacementDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Placements (with nested JSON)
    to be viewed or edited.
    """
    queryset = Placement.objects.all()
    serializer_class = PlacementDetailsSerializer