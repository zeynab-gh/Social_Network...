from django.contrib.auth.models import get_user_model
from rest_framework import generics
from .serializers import RegisterSerializer

User = get_user_model


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer




