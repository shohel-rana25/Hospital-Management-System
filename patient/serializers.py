from rest_framework import serializers
from .models import PatientModel
from django.contrib.auth.models import User


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientModel
        fields='__all__'

      
class RegistrationSerializer(serializers.ModelSerializer):
       confirm_password = serializers.CharField(required=True)

       class Meta:
              model=User
              fields=['username', 'first_name','last_name', 'email', 'password', 'confirm_password']

       def save (self):
              username =self.validated_data['username']
              first_name =self.validated_data['first_name']
              last_name =self.validated_data['last_name']
              email =self.validated_data['email']
              password =self.validated_data['password']
              confirm_password =self.validated_data['confirm_password']       

              if password!=confirm_password:
                     raise serializers.ValidationError({'error':"Password doesn't match"})    
              
              if User.objects.filter(email=email).exists():
                     raise serializers.ValidationError({'error':"email already exists"})    
              
              account=User(username=username, email=email, first_name=first_name, last_name=last_name)
              account.set_password(password)
              account.is_active=False
              account.save()
              return account


class UserLoginSerializer(serializers.Serializer):
      username=serializers.CharField(required=True)
      password=serializers.CharField(required=True)