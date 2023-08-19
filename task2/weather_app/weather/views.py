import json
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .weather_data import weather_data

@csrf_exempt
def weather_view(request, city):
    try:
        weather_info = weather_data[city]
        return JsonResponse(weather_info)
    except KeyError:
        raise Http404("City not found")

@csrf_exempt
def weather_create_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            city = data.get('city')
            temperature = data.get('temperature')
            weather = data.get('weather')

            if city and isinstance(temperature, int) and weather:
                weather_info = {
                    'temperature': temperature,
                    'weather': weather
                }
                weather_data[city] = weather_info
                return JsonResponse(weather_info, status=201)
            else:
                return HttpResponseBadRequest("Missing or invalid fields")
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")
    return HttpResponse(status=405)

@csrf_exempt
def weather_update_view(request, city):
    if request.method == 'PUT':
        if city in weather_data:
            try:
                data = json.loads(request.body)
                temperature = data.get('temperature')
                weather = data.get('weather')

                if temperature is not None:
                    weather_data[city]['temperature'] = temperature
                if weather:
                    weather_data[city]['weather'] = weather

                return JsonResponse(weather_data[city])
            except json.JSONDecodeError:
                return HttpResponseBadRequest("Invalid JSON")
        return HttpResponse(status=404)
    return HttpResponse(status=405)

@csrf_exempt
def weather_delete_view(request, city):
    if request.method == 'DELETE':
        if city in weather_data:
            del weather_data[city]
            return HttpResponse(status=204)
        return HttpResponse(status=404)
    return HttpResponse(status=405)
