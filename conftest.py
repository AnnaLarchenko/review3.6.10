import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or fr")

@pytest.fixture(scope="function")
def browser(user_language):
        # user_language = request.config.getoption("language")
        print(f"\nstart {user_language} chrome browser for test..")

        options = Options()
        options.add_experimental_option('prefs', {"intl.accept_languages": user_language})
        browser = webdriver.Chrome(options=options)

        yield browser
        print("\nquit browser..")
        browser.quit()

@pytest.fixture(scope="session")
def user_language(request):
        return request.config.getoption("language")
