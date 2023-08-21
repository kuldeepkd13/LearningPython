from django.test import TestCase
from django.urls import reverse
import json
# Create your tests here.

class postTest(TestCase):
    def create(self):
        data = {'username':"rahul", 'caption':"create"}
        response = self.client.post(reverse('create',json.dumps(data) , content_type="application/json"))
        self.assertEqual(response.status_code,200)

    def view(self):
        response = self.client.get(reverse('view' ,kwargs= {'id':'1'}))
        self.assertEqual(response.status_code,200)

    def delete(self):
        response = self.client.delete(reverse('delete' ,kwargs= {'id':'1'}))
        self.assertEqual(response.status_code,200)