# WeatherTempo

## Description

Introducing WeatherTempo, a weather forecasting API that empowers developers to integrate real-time weather data into their applications. With WeatherTempo, you can effortlessly retrieve accurate current weather information and multi-day forecasts for any city worldwide. Seamlessly access essential weather details like temperature, humidity, wind speed, and conditions in either metric or imperial units. Stay ahead of changing weather patterns, enhance user experiences, and build weather-driven applications with ease using WeatherTempo's reliable and easy-to-use API.

## Features

- Retrieve current weather data for a specific city.
- Get multi-day weather forecasts for a specific city.
- Choose between metric (Celsius) and imperial (Fahrenheit) units.
- Access essential weather details like temperature, humidity, wind speed, and conditions.
- Support for worldwide cities.

## Usage

To use WeatherTempo, you need to obtain an API key from [WeatherAPI](https://www.weatherapi.com/). Follow the steps below to get an API key for free:

1. Go to the [WeatherAPI website](https://www.weatherapi.com/).
2. Sign up for a free account or log in if you already have one.
3. Once logged in, navigate to your account settings or dashboard.
4. Locate the API key section and generate a new API key.
5. Copy the generated API key.

## API Endpoints

### Get Current Weather

Retrieve the current weather for a specific city.

Endpoint: `/weather`

Parameters:

- `city` (required): The name of the city for which to retrieve the weather.
- `units` (optional): The units of measurement for temperature, humidity, and wind speed. Default is `metric` (Celsius).

Example Usage:

GET /weather?city=London&units=metric

### Get Weather Forecast

Retrieve the weather forecast for a specific city for the next few days.

Endpoint: `/forecast`

Parameters:

- `city` (required): The name of the city for which to retrieve the forecast.
- `days` (optional): The number of days to include in the forecast. Default is 1.
- `units` (optional): The units of measurement for temperature, humidity, and wind speed. Default is `metric` (Celsius).

Example Usage:

GET /forecast?city=London&days=3&units=metric

## Dependencies

- Flask: `pip install flask`
- Requests: `pip install requests`

## Running the Application

1. Make sure you have Python 3.x installed on your system.
2. Install the required dependencies using the commands mentioned above.
3. Replace `<YOUR_API_KEY>` in the `WeatherTempo` initialization with your actual API key obtained from WeatherAPI.
4. Save the code in a file, e.g., `app.py`.
5. Open a terminal or command prompt and navigate to the directory where the file is saved.
6. Run the command: `python app.py`.
7. The Flask development server will start running on `http://localhost:5000`.
8. You can now make requests to the API endpoints mentioned above.

Note: Remember to keep your API key confidential and do not share it publicly.

## Disclaimer

Please note that WeatherTempo relies on the WeatherAPI service for weather data. Availability and accuracy of the data may be subject to the limitations and policies of WeatherAPI.
