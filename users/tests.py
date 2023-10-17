from django.test import TestCase
from django.urls import reverse
from users.models import User
from http import HTTPStatus
from users.forms import UserRegistrationForm
from users.models import User, EmailVerification
from datetime import timedelta
from django.utils.timezone import now
# Create your tests here.

class UserRegistrationViewTestCase(TestCase):

    def setUp(self) -> None:
        self.path = reverse('users:register')

    def test_user_registration_get(self):
        response = (self.client.get(self.path))
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_post_success(self):
        data = {
            'first_name': 'Vadik',
            'last_name': 'Melnik',
            'username': 'macho',
            'email': 'vadik@mail.ru',
            'password1': 'Kollege23',
            'password2': 'Kollege23',
        }
        username = data['username']
        response = (self.client.post(self.path))
        self.assertEquals(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username = username).exists())
        email_verification = EmailVerification.objects.filter(user_username = username)
        self.assertTrue(email_verification.exists())
        self.assertEquals(
            email_verification.first().expiration.date(),
            (now()+ timedelta(hours=48)).date()
        )

    def test_user_registration_post_error(self):
        username = self.data['username']
        user = User.objects.create(username = username)
        response = self.client.post(self.path, self.data)
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)

