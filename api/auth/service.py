from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class AuthService:
    def login_user(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            
            if not email or not password:
                return Response(
                    {"message": "Email and password are required"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            # try:
            #     user =
            
            user = authenticate(username=email, password=password)
            if user is not None:
                refreshToken = RefreshToken.for_user(user)
                return Response({
                    "message": "login successful",
                    "refresh": str(refreshToken),
                    "access": str(refreshToken.access_token)
                })
            return None
        except Exception as e:
            return Response(
                {"message": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )