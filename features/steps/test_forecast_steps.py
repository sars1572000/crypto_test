from pytest_bdd import scenarios, given, when, then
from pages.HomePage import HomePage

scenarios("../features/test_forecast.feature")


@given("the app is launched")
def launch_app(driver):
    pass


@when("I navigate to the 9-day forecast screen")
def navigate_to_forecast(driver):
    homepage = HomePage(driver)
    homepage.go_to_9_day_forecast()


@then("I should see the 9th day’s weather information")
def verify_ninth_day_forecast(driver):
    homepage = HomePage(driver)
    text = homepage.get_ninth_day_weather()
    print("ninth_day_forecast = " + text)
    assert text is not None and len(text) > 0
