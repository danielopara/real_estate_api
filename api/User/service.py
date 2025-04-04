import traceback

from api.models import UserAccount
from api.serializers import UserProfileSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserService:
    def create_user(self, request):
        try:
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            other_names = request.data.get('other_names')
            email = request.data.get('email')
            password = request.data.get('password')
            gender = request.data.get('gender')
            dob = request.data.get('dob')

            if not email or not password:
                return Response(
                    {"message": "Email and password are required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if User.objects.filter(username=email).exists() or User.objects.filter(email=email).exists():
                return Response(
                    {"message": "Email already exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user = User.objects.create_user(username=email, email=email, password=password)

            if user is not None:
                user_profile = UserAccount.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    dob=dob,
                    other_names=other_names,
                    gender=gender,
                    user=user
                )
                serializer = UserProfileSerializer(user_profile)
                return Response(
                    {"message": "User created successfully", "user": serializer.data},
                    status=status.HTTP_201_CREATED,
                )

            return Response(
                {"message": "User creation failed"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except Exception as e:
            return Response(
                {"message": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
            
    def list_users(self, request):
        try:
            users = UserAccount.objects.all()
            user_data = []
            for user in users:
                user_data.append({
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "other_names": user.other_names
                })
            return Response({
                'data': user_data
            })
                
        except Exception as e:
            return Response(
                {"message": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def get_auth_user(self, request):
        try:
           auth = JWTAuthentication()
           auth_result =auth.authenticate(request)
           
           if auth_result is None:
                return Response({"message": "no auth"}, status=status.HTTP_400_BAD_REQUEST)
            
           user, token = auth_result
           try:
               user_profile = UserAccount.objects.get(user=user)
           except UserAccount.DoesNotExist:
               return Response({
                   "message": 'user does not exist'
               }, status=status.HTTP_404_NOT_FOUND)
           
           profile = UserProfileSerializer(user_profile)
           return Response({
                'message': "User profile retrieved successfully",
                'profile': profile.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            error_trace = traceback.format_exc() 
            print(error_trace) 
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)