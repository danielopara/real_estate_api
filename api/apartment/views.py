from api.apartment.service import ApartmentService
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_apartment(request):
    return ApartmentService().create_apartment(request)