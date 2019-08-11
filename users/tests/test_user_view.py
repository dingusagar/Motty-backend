from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status

from django.urls import reverse

from users.models import User, UserProfile
from users.views import UserProfileViewSet
from users.serializers import UserProfileSerializer
from users.factories import UserFactory

from faker import Faker

fake = Faker()
req_factory = APIRequestFactory()


# Create your tests here.

class TestUserView(TestCase):

    def create_user_and_set_password(self, password=None):
        if not password:
            password = fake.password()
        user = UserFactory()
        user.set_password(password)
        user.save()
        return user, password

    def test_user_logging_in(self):
        client = Client()
        user, password = self.create_user_and_set_password()
        print('Setting password to ', password)
        logged_in = client.login(username=user.username, password=password)
        self.assertEquals(logged_in, True, 'user could not log in')

    def test_userprofle_updated_field_is_False_before_first_update_and_True_after_update(self):
        user, password = self.create_user_and_set_password()

        """get the id of the userprofile of the current user """
        view = UserProfileViewSet.as_view({'get': 'list'})
        request = req_factory.get(reverse('user_profile-list'))
        force_authenticate(request, user=user)  # authenticating with the created user
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """ response is a list containing one item that is the currently logged in user_profile """
        profile_id = response.data[0]['id']

        view = UserProfileViewSet.as_view({'get': 'retrieve'})
        request = req_factory.get(reverse('user_profile-detail', args=(profile_id,)))
        force_authenticate(request, user=user)  # authenticating with the created user
        response = view(request, pk=profile_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['updated'], False, 'Updated field needs to be False before the first update')

        """preparing json data for updating userprofile"""
        profile = UserProfile.objects.get(pk=profile_id)
        profile.address = fake.address()
        serializer = UserProfileSerializer(profile)
        data = serializer.data

        url = reverse('user_profile-detail', args=(profile_id,))
        request = req_factory.put(url, data, format='json')
        view = UserProfileViewSet.as_view({'put': 'update'})
        force_authenticate(request, user=user)

        response = view(request, pk=str(profile_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['updated'], True, 'Updated field needs to be true after the first update')
        # print(response.data)
