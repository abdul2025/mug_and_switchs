
from rest_framework import serializers
from account.models import  Users
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .enum import *
from .serivces import *
class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = Users
      fields = "__all__"


class CustomersTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
      token = super().get_token(user)
      return AccountService.optain_access_token(
          user=user,
          group=GroupEnum.CUSTOMERS_GROUP,
          token=token
      )