from rest_framework import serializers
from .models import adminLogin
from .models import FileUpload
from .models import Signup
from .models import Login

// This is the Api Page for file Sharing system

class FileUploadSerializer(serializers.Serializer):
      class Meta:
        model = FileUpload
        fields = ('id', 'name', 'file')

class UserSerializer(serializers.Serializer):
  class Meta:
    model = adminLogin
    fields = ['email', 'password', 'is_verified']

  def create(self, validated_data):
    return Signup.objects.create(**validated_data)

class SignupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Signup
    fields = ['Username','Email','Password','ConFirmPassword','is_Verified']

  def create(self, validated_data):
    # print(validated_data)
    return Signup.objects.create(**validated_data)
  
class LoginSerializer(serializers.Serializer):
  class Meta:
    model = Login
    fields = ['Username','Email','Password','is_Verified']

