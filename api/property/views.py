from api.property.service import PropertyService
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_property(request):
    """
    Create a new property
    """
    property_service = PropertyService()
    return property_service.create_property(request)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_all_properties(request):
    """
    list all properties
    """
    property_service = PropertyService()
    return property_service.get_all_properties(request)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_property(request):
    """
    get a property
    """
    property_service = PropertyService()
    return property_service.get_property(request)
