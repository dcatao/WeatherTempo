import requests
from flask import Flask, request, jsonify


class WeatherTempo:
    def __init__(self, api_key):
        self.base_url = 'https://api.weatherapi.com/v1/current.json'
        self.forecast_url = 'https://api.weatherapi.com/v1/forecast.json'
        self.api_key = api_key

    def get_current_weather(self, city, units='metric'):
        """
        Get the current weather for a specific city.

        Parameters:
            - city (str): The name of the city for which to retrieve the weather.
            - units (str): Optional. The units of measurement for temperature, humidity, and wind speed.
                           Default is 'metric' (Celsius).

        Returns:
            - JSON response containing the current weather information, including temperature, humidity,
              wind speed, and conditions.

        Example usage:
            GET /weather?city=London&units=metric
        """
        params = {
            'key': self.api_key,
            'q': city,
            'units': units
        }

        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()

            if 'current' in data:
                current = data['current']

                temperature = current['temp_c']
                humidity = current['humidity']
                wind_speed = current['wind_kph']

                if units == 'imperial':
                    temperature = current['temp_f']
                    humidity = current['humidity']
                    wind_speed = current['wind_mph']

                weather_data = {
                    'city': city,
                    'conditions': current['condition']['text'],
                    'temperature': temperature,
                    'humidity': humidity,
                    'wind_speed': wind_speed,
                    'units': units
                }

                return jsonify(weather_data)
            else:
                return jsonify({'error': 'Weather data not available.'})
        except requests.exceptions.RequestException as e:
            return jsonify({'error': str(e)})

    def get_weather_forecast(self, city, days=1, units='metric'):
        """
        Get the weather forecast for a specific city for the next few days.

        Parameters:
            - city (str): The name of the city for which to retrieve the forecast.
            - days (int): Optional. The number of days to include in the forecast. Default is 1.
            - units (str): Optional. The units of measurement for temperature, humidity, and wind speed.
                           Default is 'metric' (Celsius).

        Returns:
            - JSON response containing the weather forecast data for the specified city and days.

        Example usage:
            GET /forecast?city=London&days=3&units=metric
        """
        params = {
            'key': self.api_key,
            'q': city,
            'days': days,
            'units': units
        }

        try:
            response = requests.get(self.forecast_url, params=params)
            data = response.json()

            if 'forecast' in data:
                forecast_data = []
                for day in data['forecast']['forecastday']:
                    day_data = day['day']

                    temperature = day_data['avgtemp_c']
                    humidity = day_data['avghumidity']
                    wind_speed = day_data['maxwind_kph']

                    if units == 'imperial':
                        temperature = day_data['avgtemp_f']
                        humidity = day_data['avghumidity']
                        wind_speed = day_data['maxwind_mph']

                    forecast_data.append({
                        'date': day['date'],
                        'conditions': day_data['condition']['text'],
                        'temperature': temperature,
                        'humidity': humidity,
                        'wind_speed': wind_speed,
                        'units': units
                    })

                return jsonify(forecast_data)
            else:
                return jsonify({'error': 'Weather data not available.'})
        except requests.exceptions.RequestException as e:
            return jsonify({'error': str(e)})


app = Flask(__name__)
weather_app = WeatherTempo(api_key='<YOUR_API_KEY>')


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is missing.'})

    units = request.args.get('units', 'metric')
    return weather_app.get_current_weather(city, units)


@app.route('/forecast', methods=['GET'])
def get_forecast():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is missing.'})

    units = request.args.get('units', 'metric')
    days = int(request.args.get('days', 1))
    return weather_app.get_weather_forecast(city, days, units)


if __name__ == '__main__':
    app.run()
