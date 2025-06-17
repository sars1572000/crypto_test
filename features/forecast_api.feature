@api
Feature: Hong Kong 9-day Weather Forecast

  Scenario: Get relative humidity for the day after tomorrow
    Given the 9-day weather forecast API is available
    When I request the weather data
    Then the response should be successful
    And I should see the relative humidity for the day after tomorrow