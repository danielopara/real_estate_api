from api.models import Property, UserAccount
from api.serializers import PropertySerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


class PropertyService():
    def create_property(self, request):
        try:
            name = request.data.get('name')
            state = request.data.get('state')
            city = request.data.get('city')
            apartments = request.data.get('apartments')
            address = request.data.get('address')
            
            if Property.objects.filter(address=address).exists():
                return Response(
                    {'message': "property with address already exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            user = UserAccount.objects.get(user = request.user)
            property = Property.objects.create(
                name=name,
                state=state,
                city=city,
                address=address,
                apartments=apartments,
                owner=user
            )
            property_data = PropertySerializer(property)
            return Response(
                {'message': "property created successfully", 'property': property_data.data},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"message": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    
    def get_all_properties(self, request):
        try:
            properties = Property.objects.all()
            serializer = PropertySerializer(properties, many=True)
            return Response({
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"message": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    
    def get_property(self, request):
        try:
            property_id = request.GET.get('property_id')
            
            try:
                property = Property.objects.get(id=property_id)
            except Property.DoesNotExist:
                return Response(
                    {'message': "property not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = PropertySerializer(property)
            return Response({
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"message": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )