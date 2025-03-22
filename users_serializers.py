from rest_framework import serializers
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Admin
        fields = ['email', 'password']
    
    def create(self, validated_data):
        admin = Admin.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return admin