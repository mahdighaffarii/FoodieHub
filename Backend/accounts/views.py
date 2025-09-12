from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserRegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer
    
# accounts/views.py
from .serializers import UserDetailSerializer
from rest_framework.permissions import IsAuthenticated

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user