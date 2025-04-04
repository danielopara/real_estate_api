from api.auth.service import AuthService
from rest_framework.decorators import api_view


@api_view(['POST'])
def login_user(request):
    auth_service = AuthService()
    return auth_service.login_user(request)