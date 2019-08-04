from django.test import TestCase, Client
from django.urls import reverse

HEADER = {"HTTP_X_REQUESTED_WITH": "XMLHttpRequest"}
URL = reverse("suggestion:auto_complete")


class AutoCompleteTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_invalid_ajax_request(self):
        """
        checking invalid request responding 400
        """
        response = self.client.get(URL)
        self.assertEqual(response.status_code, 400)

    def test_valid_ajax_request(self):
        """
        testing valid request status code
        """
        response = self.client.get(URL, {"word": "a"}, **HEADER)
        self.assertEqual(response.status_code, 200)

    def test_response_content_type(self):
        """
        testing if response content type is JSON
        """
        response = self.client.get(URL, {"word": "a"}, **HEADER)
        self.assertEqual(response["Content-Type"], "application/json")
    # def test_
