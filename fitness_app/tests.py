from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch
from fitness_app.models import FitnessPlan
from accounts.models import UserDetail

User = get_user_model()

class FitnessModelTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testusername',
            'password': 'strongpassword1234',
        }
        self.user = User.objects.create_user(**self.user_data)

        self.user_detail_data = {
            'user': self.user,
            'first_name': 'testfirst_name',
            'last_name': 'testlast_name',
            'phone_number': '123456789',
            'buyi': '170',
            'vazni': '80',
            'jinsi': 'testjinsi',
            'maqsadi': 'testmaqsadi',
        }
        self.user_detail, created = UserDetail.objects.get_or_create(
            user=self.user,
            defaults=self.user_detail_data
        )

        self.user_hisobot_data = {
            'user': self.user,
            'Kunlik': 'testkunlik',
            'Haftalik': 'testhaftalik',
            'Oylik': 'testoylik',
            'Yillik': 'testylik',
        }

        self.user_hisobot_detail, created = UserDetail.objects.get_or_create(
            user=self.user,
            defaults=self.user_hisobot_data
        )

        if not created:
            for key, value in self.user_detail_data.items():
                setattr(self.user_detail, key, value)
            self.user_detail.save()

    def test_hisobot_list(self):
        url = reverse('hisobot_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),4)

    def test_hisobot_detail(self):
        url = reverse('hisobot_list',args=[self.hisobot.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_hisobot_create(self):
        url = reverse('hisobot_list',args=[self.hisobot.pk])
        data = {'kunlik': 'testkunlik',
                'haftalik': 'testhaftalik',
                'oylik': 'testoylik',
                'ylik': 'testylik',
                }
        response = self.client.post(url, data,format='json')
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)

    def test_hisobot_update(self):
        url = reverse('hisobot_list',args=[self.hisobot.pk])
        data = {'kunlik': 'testkunlik',
                'haftalik': 'testhaftalik',
                'oylik': 'testoylik',
                'ylik': 'testylik',
                }
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code , status.HTTP_200_OK)

    def test_hisobot_delete(self):
        url = reverse('hisobot_list',args=[self.hisobot.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
