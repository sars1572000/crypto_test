import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        appPackage='hko.MyObservatory_v1_0',
        appActivity='hko.homepage3.HomepageActivity',
        udid = '{device udid}',
        noReset=True
    )

    appium_server_url = 'http://localhost:4723'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def context():
    return {}