from datetime import datetime
from weather_forecast import WeatherForecast

if __name__ == "__main__":
    API_KEY = 'f7d264581a9b460f87f150031242202'
    weather_api_url = 'https://api.weatherapi.com/v1/forecast.json'

    weather_forecast = WeatherForecast("weather_data.json", weather_api_url, API_KEY)

    while True:
        location = input("Enter location (or 'x' to exit): ")
        if location.lower() == 'x':
            break

        datetime_str = datetime.now().strftime("%Y-%m-%d %H:%M")  # Current datetime

        forecast_data = weather_forecast.get_weather_forecast(location, datetime_str)
        if forecast_data:
            print("Weather forecast:")
            print("-" * 20)
            if 'current' in forecast_data:
                print(f"Temperature: {forecast_data['current']['temp_c']}°C")
                print(f"Humidity: {forecast_data['current']['humidity']}%")
                print(f"Cloudiness: {forecast_data['current']['cloud']}%")
                print(f"Wind Speed: {forecast_data['current']['wind_kph']} km/h")
                print(f"Pressure: {forecast_data['current']['pressure_mb']} mb")
            else:
                print("Current weather data not available.")
            if 'forecast' in forecast_data and 'forecastday' in forecast_data['forecast']:
                print(
                    f"Chance of Rain: {forecast_data['forecast']['forecastday'][0]['day'].get('daily_chance_of_rain', 'N/A')}%")
                print(
                    f"Chance of Snow: {forecast_data['forecast']['forecastday'][0]['day'].get('daily_chance_of_snow', 'N/A')}%")
            else:
                print("Forecast data not available.")
            print("-" * 20)  # Separator
        else:
            print("Failed to fetch weather forecast.")

        weather_forecast.save_weather_forecast(location, datetime_str, forecast_data)
