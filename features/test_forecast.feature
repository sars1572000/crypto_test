@app
Feature: 9-day weather forecast

  Scenario: Check the 9th day’s weather forecast
    Given the app is launched
    When I navigate to the 9-day forecast screen
    Then I should see the 9th day’s weather information