from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions
from .models import Organization, Role, User
from .serializers import OrganizationSerializer, RoleSerializer, UserSerializer
from .permissions import IsSuperAdmin, IsAdmin, IsManager, IsMember, IsOwner

class OrganizationListView(APIView):
    permission_classes = [IsAuthenticated]  # All authenticated users can list organizations

    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)

class OrganizationDetailView(APIView):
    permission_classes = [IsOwner]  # Only super admins or owners can access details

    def get(self, request, pk):
        try:
            organization = Organization.objects.get(pk=pk)
        except Organization.DoesNotExist:
            return Response({'error': 'Organization not found'}, status=404)
        serializer = OrganizationSerializer(organization)
        return Response(serializer.data)

    # Add similar views with appropriate permissions for other models (Role, User)

class UserCreateView(APIView):
    permission_classes = [IsSuperAdmin | IsAdmin]  # Only super admins or admins can create users

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Add similar views for update and delete operations with appropriate permissions
