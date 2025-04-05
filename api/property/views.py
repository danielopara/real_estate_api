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
