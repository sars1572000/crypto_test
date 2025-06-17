# MyObservatory 9-Day Forecast API & UI Automation

This is a mobile and API automation testing project for the **MyObservatory** app from the **Hong Kong Observatory**.  
The goal is to automate and validate the **9-day weather forecast** feature via **Appium UI automation** and **API testing** using `pytest-bdd`.

---

## 📁 Project Structure

├── features
│ ├── steps
│ │ ├── test_forecast_api_steps.py # Step definitions for API test
│ │ └── test_forecast_steps.py # Step definitions for UI test
│ ├── forecast_api.feature # API BDD feature
│ └── test_forecast.feature # UI BDD feature
├── pages
│ └── HomePage.py # Page Object for forecast page (Appium)
├── utils
│ └── weather_api.py # Weather API client 
├── conftest.py # test fixtures
├── pytest.ini # Pytest configuration
└── requirements.txt # Python dependencies


---

## ⚙️ Setup Guide

### 🔧 Prerequisites

- Python 3.11.9+
- [Appium Server](https://appium.io/) running (for mobile UI automation)
- Android Emulator or physical device connected
- You need to have the MyObservatory mobile app installed and launched to the home screen.
- The udid in conftest.py needs to be replaced with the UDID of the connected device.



### 📦 Installation

pip install -r requirements.txt

### To run API testing:
pytest -m "api"

### To run APP testing: (Make sure the Appium server is started and the device is connected)
pytest -m "app"

### 🧱 Design & Architecture
✅ API Testing
- Implemented Gherkin-style test scenarios using pytest-bdd
- Abstracted API request logic into utils/weather_api.py for reusability and maintainability
- Used @when and @then steps to validate the response status code and parse the JSON structure
- Extracted the relative humidity for the day after tomorrow to assert the correctness of the response

✅ Mobile UI Testing
- Applied the Page Object Model (POM) to encapsulate UI elements and actions
- UI elements and methods are defined in pages/HomePage.py
- Test scenarios are written in .feature files and implemented in steps/test_forecast_steps.py
- This design separates UI interactions from test logic, making the framework more scalable and easier to maintain

###  Test Cases
🎯 API: features/forecast_api.feature
Validate that the API response status code is 200
- Verify the correctness of the returned JSON structure
- Extract the forecast date and relative humidity range (e.g., 60% - 85%) for the day after tomorrow (today + 2)

📱 UI: features/test_forecast.feature
- Launch the MyObservatory mobile app
- Navigate to the "9-day forecast" section
- Check the 9th day’s weather forecast from 9-day forecast screen


