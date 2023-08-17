from django.test import TestCase
from django.urls import reverse

class WeatherViewTest(TestCase):

    def test_valid_city(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'New York'}))
        self.assertEqual(response.status_code, 200)
    
    def test_invalid_city(self):
       response = self.client.get(reverse('weather', kwargs={'city': 'InvalidCity'}))
       self.assertEqual(response.status_code, 404)

    def test_city_with_charcter(self):
       response = self.client.get(reverse('weather', kwargs={'city': 'San_Francisco'}))
       self.assertEqual(response.status_code, 404)

    def test_city_with_empty(self):
      response = self.client.get(reverse('weather', kwargs={'city': ' '}))
      self.assertEqual(response.status_code, 404)
      self.assertJSONEqual(str(response.content, encoding='utf-8'), {'error': 'Provide a valid city name'})

