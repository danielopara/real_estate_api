from api.apartment.service import ApartmentService
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_apartment(request):
    return ApartmentService().create_apartment(request)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def return_apartments(request):
    return ApartmentService().return_property_apartment(request)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_apartments(request):
    return ApartmentService().get_apartments(request)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_apartment(request):
    return ApartmentService().update_apartment(request)