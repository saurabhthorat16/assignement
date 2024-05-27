from rest_framework import serializers
from .models import Organization, Role, User

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SlugRelatedField(many=True, queryset=Role.objects.all(), slug_field='name')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'organization', 'roles')
