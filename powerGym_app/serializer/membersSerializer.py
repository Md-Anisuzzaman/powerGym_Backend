from rest_framework import serializers
from ..model.membersModel import Member
from django.contrib.auth.hashers import make_password


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        extra_kwargs = {"password": {"write_only": True,"required":False,"allow_null":True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        print("my password", password)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            hashed_password = make_password(password)
            instance.password = hashed_password
            print("my instance",instance)
        instance.save()
        return instance
    
    
    

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['full_name', 'email', 'password']
        # fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            }  # Ensure password is not exposed in responses

    def validate_password(self, value):
        """
        Custom password validation logic.
        """
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must include at least one numeric digit.")
        if not any(char.isalpha() for char in value):
            raise serializers.ValidationError("Password must include at least one letter.")
        return value

    def create(self, validated_data):
        """
        Custom create logic to hash the password before saving.
        """
        password = validated_data.pop('password')  # Extract password from validated data
        validated_data['password'] = make_password(password)  # Hash the password
        return super().create(validated_data)  # Use default create to save the instance

