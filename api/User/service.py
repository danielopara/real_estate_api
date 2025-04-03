from api.models import UserAccount
from api.serializers import UserProfileSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response


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

            if user:
                user_profile = UserAccount.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
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
