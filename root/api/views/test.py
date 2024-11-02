from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from ..views.polls import PollList
from ..views.users import UserRegisterAPIView

class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = PollList.as_view()
        print(self.view,"==============")
        self.uri = '/api/poll/list/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
            'Expected Response Code 200, received {0} instead.'
            .format(response.status_code))
    