import requests
from django.shortcuts import render

API_KEY = 'df9610c8f8a5b9f524b04c0605860b2f'


def get_weather(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST['city']
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city,
                'temp': data['list'][0]['main']['temp'],
                'humidity': data['list'][0]['main']['humidity'],
                'wind': data['list'][0]['wind']['speed'],
                'icon': data['list'][0]['weather'][0]['icon'],
                'forecast': [
                    {
                        'dt_txt': entry['dt_txt'],
                        'temp': entry['main']['temp']
                    } for entry in data['list'][:7]
                ]
            }
        else:
            weather_data = {'error': 'City not found'}

    return render(request, 'index.html', {'weather': weather_data})
