from rest_framework import serializers
from django.contrib.auth.models import User  # Import the default User model
from .models import Game

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)  # Add the confirm_password field
    class Meta:
        model = User  # Use the default User model
        fields = ['username', 'password', 'email', 'confirm_password']

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password', None)  # Remove confirm_password from the data
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Use the default User model
        fields = ['username', 'password']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'