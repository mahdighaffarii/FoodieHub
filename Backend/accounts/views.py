from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserRegisterSerializer

class RegisterView(generics.CreateAPIView):
    """
    API view for user registration.
    Allows any user (authenticated or not) to create a new user account.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer