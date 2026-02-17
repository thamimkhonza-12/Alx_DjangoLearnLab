from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


# User Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # This is REQUIRED for the test
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

        # Create token automatically
        Token.objects.create(user=user)

        return user


# User Login Serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if user is None:
            raise serializers.ValidationError("Invalid credentials")

        token, created = Token.objects.get_or_create(user=user)

        return {
            "username": user.username,
            "token": token.key
        }


# User Serializer (optional but useful)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
