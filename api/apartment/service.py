from api.models import Apartment, Property
from api.serializers import ApartmentSerializer
from rest_framework import status
from rest_framework.response import Response


class ApartmentService():
    
    def create_apartment(self, request):
        try:
            property_id = request.data.get('property_id')
            rooms = request.data.get('rooms')
            toilets = request.data.get('toilets')
            bathrooms = request.data.get('bathrooms')
            description = request.data.get('description')
            
            try:
                property = Property.objects.get(id=property_id)
            except Property.DoesNotExist:
                return Response(
                    {'message': "property does not exist"},
                    status=status.HTTP_404_NOT_FOUND
                )
            apartment_count = Apartment.objects.filter(property=property).count()
            
            if apartment_count >= property.apartments:
                return Response(
                    {
                        'message': "number of apartments cannot be exceeded"
                    }, status=status.HTTP_400_BAD_REQUEST
                )
                
            data = Apartment.objects.create(
                property = property,
                rooms = rooms,
                toilets = toilets,
                bathrooms = bathrooms,
                description = description,
                apartment_number = apartment_count + 1
            )
            apartment = ApartmentSerializer(data)
            return Response(
                {
                    'message': 'apartment created',
                    'data': apartment.data            
                },
                status = status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"message": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )