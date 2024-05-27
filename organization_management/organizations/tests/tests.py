from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from organization_management.organizations.models import Organization
from organization_management.organizations.serializers import OrganizationSerializer

class OrganizationListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.organization = Organization.objects.create(name='My Organization')

    def test_list_organizations_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/organizations/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        serializer = OrganizationSerializer(self.organization)
        self.assertEqual(response.data['results'][0], serializer.data)

    def test_list_organizations_unauthenticated(self):
        response = self.client.get('/api/organizations/')
        self.assertEqual(response.status_code, 403)  # Adjust based on permission denial code
