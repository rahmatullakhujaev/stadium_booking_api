from st_booking_api.user.models import User, Permission, Role
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'first_name', 'last_name', 'is_active', 'is_superuser', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name', 'code_name']


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['name', 'code_name']


class RolePermissionSerializer(serializers.Serializer):
    permission = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), many=True)

    class Meta:
        model = Role
        fields = ['permission']