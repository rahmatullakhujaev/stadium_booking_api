from rest_framework import serializers
from .models import User, Role, Permission



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'



class PermissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'