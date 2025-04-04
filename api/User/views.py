from api.user.service import UserService
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def create_user(request):
    """
    Create a new user account.
    """
    user_service = UserService()
    return user_service.create_user(request)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    return UserService().get_auth_user(request)
