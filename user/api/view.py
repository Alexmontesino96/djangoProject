from rest_framework.views import APIView
from rest_framework.response import Response
from user.api.serializer import UserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from user.api.serializer import UserSerializer, UserUpdateSerializer
from user.models import User


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):

        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, data=request.data)
        print(user.first_name, "first_name")
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
