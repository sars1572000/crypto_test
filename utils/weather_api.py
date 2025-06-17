import requests
from datetime import datetime, timedelta

BASE_URL = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"

def get_forecast(data_type="fnd", lang="en"):
    """
    Send Observatory API request
    :param data_type: data type (default 'fnd' for 9-day forecast)
    :param lang: language ('en' or 'tc')
    :return: requests.Response
    """
    params = {
        "dataType": data_type,
        "lang": lang
    }
    response = requests.get(BASE_URL, params=params)
    return response

def get_day_after_tomorrow_humidity(json_data):
    # Today + Two days = the day after tomorrow
    today = datetime.now()
    day_after_tomorrow = today + timedelta(days=2)
    day_str = day_after_tomorrow.strftime("%Y%m%d")

    print(f"Query date：{day_after_tomorrow.strftime('%Y-%m-%d')}")

    # Search for the relative humidity for the corresponding date
    for day in json_data["weatherForecast"]:
        if day["forecastDate"] == day_str:
            rel_humidity = day.get("forecastMaxrh", {}).get("value"), day.get("forecastMinrh", {}).get("value")
            return rel_humidity

    raise Exception("It is not possible to find relative humidity information for the day after tomorrow from the API data.")

