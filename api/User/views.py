from api.user.service import UserService
from rest_framework.decorators import api_view


@api_view(['POST'])
def create_user(request):
    """
    Create a new user account.
    """
    user_service = UserService()
    return user_service.create_user(request)