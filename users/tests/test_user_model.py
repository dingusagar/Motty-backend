from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory, force_authenticate


from organisation.factories import CompanyFactory
from organisation.models import Company
from users.models import User, UserProfile

from users.factories import UserFactory

from django.db.utils import IntegrityError
from faker import Faker

fake = Faker()
req_factory = APIRequestFactory()


# Create your tests here.

class TestUserModel(TestCase):

    def test_user_profile_gets_created_with_user_creation(self):
        user = UserFactory()
        try:
            print('Userprofile : ', user.userprofile)
        except AttributeError:
            self.fail('user profile not created with user')

    def test_userprofile_to_user_connection_cannot_be_modified(self):
        user1 = UserFactory()
        newuser = UserFactory()
        profile = user1.userprofile

        try:
            profile.user = newuser
            profile.save()
        except IntegrityError as e:
            print('Cannot modify userprofile to user relation', e)

    def test_assign_admin_status_to_user_based_on_whether_they_are_the_first_user_in_the_company(self):
        """ user1 is the first user with the email domain freshworks.com, which means he should be assigned as the
        admin """
        user1 = UserFactory(email='xywd@freshworks.com')
        email = user1.email
        domain = email.split('@')[1]

        company_present = Company.objects.filter(domain=domain).exists()
        self.assertFalse(company_present, 'freshworks company is already present..test cannot proceed')
        self.assertEqual(user1.mode, User.COMPANY_ADMIN,
                         'user1 is not made the admin even though he is the first user in company')

    def test_assign_employee_status_to_user_if_they_are_the_not_first_user_in_the_company(self):
        """ user2 from freshworks company is the second user to login the company, he is given employee status only"""

        company = CompanyFactory(domain='freshworks.com')
        user2 = UserFactory(email='ekwoej@freshworks.com')

        self.assertEqual(user2.mode, User.COMPANY_EMP)
