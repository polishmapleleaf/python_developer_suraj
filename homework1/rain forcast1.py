import requests
import json
from datetime import date, timedelta

CACHE_FILENAME = "weather_log.json"
#Location - krakow, centralna
LATITUDE = 50.0685
LONGITUDE = 19.9479
API_URL = "https://api.open-meteo.com/v1/forecast"

def load_cache():
    try:
        with open(CACHE_FILENAME, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_cache(cache_data):
    with open(CACHE_FILENAME, 'w') as f:
        json.dump(cache_data, f, indent=4)




def get_date_input():
    user_input = input("Enter a date (YYYY-mm-dd) to check for rain (leave empty for tomorrow): ")
    if not user_input:
        tomorrow = date.today() + timedelta(days=1)
        return tomorrow.strftime("%Y-%m-%d")
    return user_input



def fetch_weather_from_api(check_date):
    print(f"Fetching weather data from API for {check_date}...")
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "daily": "precipitation_sum",
        "timezone": "Europe/krakow",
        "start_date": check_date,
        "end_date": check_date
    }
    try:
        response = requests.get(API_URL, params=params)
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

def get_precipitation_status(value):
    if value is None or value < 0:
        return "I don't know if it will rain."
    elif value > 0.0:
        return f"It will rain. Precipitation: {value}mm"
    else:
        return "It will not rain"


def main():
    weather_cache = load_cache()
    target_date = get_date_input()
    try:
        date.fromisoformat(target_date)
    except ValueError:
        print("Invalid date format. Please use YYYY-mm-dd ")
        return

    if target_date in weather_cache:
        print(f"Result for {target_date} found in cache.")
        precipitation_value = weather_cache[target_date]
    else:
        precipitation_value = fetch_weather_from_api(target_date)

        if precipitation_value is not None:
            weather_cache[target_date] = precipitation_value
            save_cache(weather_cache)

    status = get_precipitation_status(precipitation_value)
    print(f"\nWeather for {target_date}:")
    print(status)

if __name__ == "__main__":
    main()