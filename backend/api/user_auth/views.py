from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import StudentModel
from .serializers import StudentSerializers, MyTokenObtainPairSerializer, LogoutSerializer
from rest_framework.response import Response


class Home(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        response = Response()

        response.set_cookie(key='jwt', value="test", httponly=True)
        response.data = {
            "Name": "Aditya Raj",
            "mobile": "8271388851",
            "status": "success"
        }

        return response


class MyTokenObtainPairView(TokenObtainPairView):

    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data_dict = {
            "status": "success",
            "data": "logout successfully"
        }

        return Response(data_dict, status=status.HTTP_204_NO_CONTENT)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all().order_by('first_name')
    serializer_class = StudentSerializers

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
