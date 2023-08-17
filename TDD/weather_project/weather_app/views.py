from django.http import JsonResponse

def weather_view(request, city):
     weather_data = {
     'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
     'New York': {'temperature': 20, 'weather': 'Sunny'},
     'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
     'Seattle': {'temperature': 10, 'weather': 'Rainy'},
     'Austin': {'temperature': 32, 'weather': 'Hot'},
     }

     if city==' ':
        return JsonResponse({'error': 'Provide a valid city name'}, status=404)
     city_data = weather_data.get(city)
    
     if city_data is None:
        return JsonResponse({'error': 'City not found'}, status=404)
    
     return JsonResponse(city_data)
