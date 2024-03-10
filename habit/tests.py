from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from habit.models import Habit
from users.models import User


class HabitAPITest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='testuser@mail,com',
            is_superuser=True,
            is_staff=True
        )
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            owner=self.user,
            place='test_place',
            time='12:00:00',
            action='test_action',
            period='HOUR',
            reward='test_reward',
            duration='00:01:00',
        )

    def test_create_habit(self):
        habit_data = {
            'owner': '1',
            'place': 'nice_place',
            'time': '12:00:00',
            'action': 'nice_action',
            'is_nice_habit': True,
            'period': 'HOUR',
            'duration': '00:01:00',
        }
        response = self.client.post(
            '/habit/create/',
            data=habit_data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 2, 'place': 'nice_place', 'time': '12:00:00', 'action': 'nice_action', 'is_nice_habit': True,
             'period': 'HOUR', 'reward': None, 'duration': '00:01:00', 'is_public': False, 'owner': 1,
             'nice_habit': None}
        )

    def test_list_habit(self):
        response = self.client.get(
            '/habit/list/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        update_data = {
            'action': 'update_action',
        }

        response = self.client.patch(
            '/habit/update/1/',
            data=update_data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'place': 'test_place', 'time': '12:00:00', 'action': 'update_action', 'is_nice_habit': False,
             'period': 'HOUR', 'reward': 'test_reward', 'duration': '00:01:00', 'is_public': False, 'owner': 3,
             'nice_habit': None}

        )

    def test_delete_habit(self):
        response = self.client.delete(
            '/habit/delete/1/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
