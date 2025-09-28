import requests
import json
from datetime import date, timedelta



class WeatherForecast:
    CACHE_FILENAME = "weather_log.json"
    API_URL = "https://api.open-meteo.com/v1/forecast"
    # location Cracow
    LATITUDE = 50.0685
    LONGITUDE = 19.9479

    def __init__(self):
        self._cache = self._load_cache()

    def _load_cache(self):
        try:
            with open(self.CACHE_FILENAME, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_cache(self):
        with open(self.CACHE_FILENAME, 'w') as f:
            json.dump(self._cache, f, indent=4)

    def _fetch_from_api(self, check_date):
        print(f"Fetching weather data from API for {check_date}...")
        params = {
            "latitude": self.LATITUDE,
            "longitude": self.LONGITUDE,
            "daily": "precipitation_sum",
            "timezone": "Europe/krakow",
            "start_date": check_date,
            "end_date": check_date
        }
        try:
            response = requests.get(self.API_URL, params=params)
            response.raise_for_status()
            data = response.json()
            precipitation = data.get("daily", {}).get("precipitation_sum", [None])[0]
            return precipitation
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return None
        except (KeyError, IndexError):
            print("Could not parse precipitation data from API response")
            return None

    def __setitem__(self, date_key, value):
        self._cache[date_key] = value
        self._save_cache()
        print(f"Manually set forecast for {date_key}. Cache update")

    def __getitem__(self, date_key):
        if date_key in self._cache:
            print(f"Result for {date_key} found in cache")
            return self._cache[date_key]
        else:
            precipitation = self._fetch_from_api(date_key)
            if precipitation is not None:
                self._cache[date_key] = precipitation
                self._save_cache()
            return precipitation

    def __iter__(self):
        return iter(self._cache.keys())

    def items(self):
        for date_key, value in self._cache.items():
            yield (date_key, value)

def get_date_input():
    user_input = input("Enter a date (YYYY-mm-dd) to check for rain (leave empty for tomorrow): ")
    if not user_input:
        tomorrow = date.today() + timedelta(days=1)
        return tomorrow.strftime("%Y-%m-%d")
    return user_input

def get_precipitation_status(value):
    if value is None or value < 0:
        return "I don't know if it will rain."
    elif value > 0.0:
        return f"It will rain. Precipitation: {value}mm"
    else:
        return "It will not rain."

def main():
    weather_forecast = WeatherForecast()
    target_date = get_date_input()

    try:
        date.fromisoformat(target_date)
    except ValueError:
        print("Invalid date format. Please use YYYY-mm-dd.")
        return


    precipitation_value = weather_forecast[target_date]
    status = get_precipitation_status(precipitation_value)
    print(f"\nWeather for {target_date}:")
    print(status)

    print("\n--- Demonstrating class functionality ---")
    print("Dates with cached forecasts (using __iter__):")
    for day in weather_forecast:
        print(f"- {day}")

    print("\nCached (date, precipitation) items (using .items()):")
    for d, p in weather_forecast.items():
        print(f"- {d}: {p}mm")
    print("---------------------------------------")

if __name__ == "__main__":
    main()

