
from rest_framework import permissions

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import UserSerializer, RegisterUserSerializer
from .models import User
# Create your views here.


class ListUsers(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CreateUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request, format=None):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
