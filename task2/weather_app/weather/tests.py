from django.test import TestCase
from django.urls import reverse
from .weather_data import weather_data
import json

class WeatherCRUDTest(TestCase):

    def test_get_weather(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'San Francisco'}))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), weather_data['San Francisco'])

    def test_create_weather(self):
        new_data = {'city': 'Chicago', 'temperature': 18, 'weather': 'Cloudy'}
        response = self.client.post(reverse('create_weather'), json.dumps(new_data),content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(weather_data['Chicago'], new_data)

    def test_create_weather_invalid_data(self):
        response = self.client.post(reverse('create_weather'), json.dumps({'city': 'Miami'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_update_weather(self):
        updated_data = {'temperature': 28}
        response = self.client.put(reverse('update_weather', kwargs={'city': 'New York'}),
                                   json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(weather_data['New York']['temperature'], updated_data['temperature'])

    def test_update_weather_invalid_json(self):
        response = self.client.put(reverse('update_weather', kwargs={'city': 'New York'}),
                                   'invalid json', content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete_weather(self):
        response = self.client.delete(reverse('delete_weather', kwargs={'city': 'Los Angeles'}))
        self.assertEqual(response.status_code, 204)
        self.assertNotIn('Los Angeles', weather_data)

    def test_delete_weather_not_found(self):
        response = self.client.delete(reverse('delete_weather', kwargs={'city': 'Miami'}))
        self.assertEqual(response.status_code, 404)
