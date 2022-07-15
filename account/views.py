from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework.response import Response

class CustomersTokenObtainPairView(TokenObtainPairView):

    def post(self, request):
        serializer = CustomersTokenObtainPairSerializer(
            data=request.data)
        
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('username'))
        return Response(serializer.validated_data)