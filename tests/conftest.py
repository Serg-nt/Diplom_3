import pytest
import requests
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..data.urls import BASE_URL_API, BASE_URL
from ..data.data import PASSWORD, NAME, generate_random_email
from ..page_objects.auth_page import AuthPage
from ..page_objects.main_page import MainPage


@pytest.fixture(params=['chrome', 'firefox'])
def browser(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome()
    else:
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox()

    yield driver
    driver.quit()


@pytest.fixture
def registered_user():
    """Фикстура создает пользователя через API и возвращает данные"""
    with allure.step("Создание пользователя через API"):
        email = generate_random_email()
        register_response = requests.post(
            f"{BASE_URL_API}/auth/register",
            json={
                "email": email,
                "password": PASSWORD,
                "name": NAME
            }
        )
        assert register_response.status_code == 200, "Ошибка регистрации пользователя"

    yield {
        "email": email,
        "name": NAME
    }

    # Пост-условие - удаление пользователя
    with allure.step("Удаление пользователя через API"):
        login_resp = requests.post(
            f"{BASE_URL_API}/auth/login",
            json={"email": email, "password": PASSWORD}
        )
        token = login_resp.json()["accessToken"].split()[-1]
        requests.delete(
            f"{BASE_URL_API}/auth/user",
            headers={"Authorization": f"Bearer {token}"}
        )

@pytest.fixture
def auth_user(browser, registered_user):
    """Фикстура авторизует пользователя через UI"""
    with allure.step("Авторизация пользователя через UI"):
        auth_page = AuthPage(browser)
        main_page = MainPage(browser)

        # Открываем главную страницу
        main_page.open()

        # Переходим в личный кабинет
        main_page.click_personal_account_when_clickable()

        # Вводим данные для авторизации
        auth_page.enter_email(registered_user["email"])
        auth_page.enter_password(PASSWORD)
        auth_page.click_login_button()

        # Ожидаем успешной авторизации
        WebDriverWait(browser, 10).until(
            lambda d: d.execute_script(
                'return localStorage.getItem("accessToken") !== null'
            )
        )
        WebDriverWait(browser, 10).until(
            EC.url_contains(BASE_URL)
        )

    yield registered_user