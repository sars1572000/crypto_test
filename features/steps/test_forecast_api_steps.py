from pytest_bdd import scenarios, given, when, then
from utils.weather_api import get_forecast, get_day_after_tomorrow_humidity

scenarios('../features/forecast_api.feature')

@given("the 9-day weather forecast API is available")
def api_available():
    pass  # just a placeholder for now

@when("I request the weather data")
def send_api_request(context):
    response = get_forecast(data_type="fnd", lang="en")
    context["response"] = response
    context["json"] = response.json()

@then("the response should be successful")
def check_status_code(context):
    assert context["response"].status_code == 200

@then("I should see the relative humidity for the day after tomorrow")
def check_humidity(context):
    humidity = get_day_after_tomorrow_humidity(context["json"])
    assert humidity is not None, "Humidity data not found for the day after tomorrow"
    print(f"Relative humidity (RH range): {humidity[1]}% - {humidity[0]}%")
