from django.test import TestCase , Client
from django.contrib.auth import get_user_model
from accounts.models import UserDetail

User = get_user_model()

class AIModelTest(TestCase):
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
        self.user_detail , created = UserDetail.objects.get_or_create(
            user=self.user,
            defaults=self.user_detail_data
        )

        if not created:
            for key , value in self.user_detail_data.items():
                setattr(self.user_detail , key , value)
            self.user_detail.save()

        self.client = Client()
        self.client.force_login(self.user)

        @patch('ai_app.views.requests.post')
        def test_ai_response_with_user_profile(self,mock_post):
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = {
                'choices': [{'message': {'content': 'Sizga mos mashg`ulot rejasi tayyor!'}}]
            }



