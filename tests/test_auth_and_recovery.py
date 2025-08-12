import allure

from ..data.urls import ORDER_HISTORY_URL, LOGIN_URL
from ..page_objects.auth_page import AuthPage
from ..page_objects.main_page import MainPage


@allure.epic("Авторизация и восстановление пароля")
class TestAuthAndRecovery:

    @allure.title("Восстановление пароля - позитивный сценарий")
    def test_password_recovery_positive(self, browser, registered_user):
        """
        Проверяет:
        1. Переход на страницу восстановления пароля
        2. Ввод валидной почты
        3. Успешное получение кода восстановления
        """
        main_page = MainPage(browser)
        auth_page = AuthPage(browser)

        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Кликнуть на кнопку Личный кабинет"):
            main_page.click_personal_account_when_clickable()

        with allure.step("Кликнуть на ссылку Восстановить пароль"):
            auth_page.click_restore_password_link()

        with allure.step("Ввести корректный email"):
            auth_page.enter_email(registered_user["email"])

        with allure.step("Кликнуть на кнопку Восстановить"):
            auth_page.click_restore_button()

        with allure.step("Кликнуть по иконке глаза для показа/скрытия пароля"):
            auth_page.click_password_toggle_icon()

        with allure.step("Проверить видимость пароля"):
            assert auth_page.is_password_visible(), (
                "Пароль не отображается (тип поля должен быть 'text')"
            )

    @allure.title("Переход в Историю заказов из личного кабинета")
    def test_navigate_to_personal_account(self, auth_user, browser):
        """
        Проверяет:
        1. Вход под существующим пользователем
        2. Переход в Личный кабинет
        3. Переход в пункт История заказов
        """

        main_page = MainPage(browser)
        auth_page = AuthPage(browser)

        with allure.step("Кликнуть на кнопку Личный кабинет"):
            main_page.click_personal_account_when_clickable()

        with allure.step("Кликнуть на раздел История заказов"):
            auth_page.click_order_history_when_clickable()

        with allure.step("Проверить переход на страницу История заказов"):
            current_url = auth_page.verify_opened()
            assert ORDER_HISTORY_URL in current_url

    @allure.title("Выход из личного кабинета")
    def test_logout_from_account_successfully(self, auth_user, browser):
        """
        Проверяет:
        1. Вход под существующим пользователем
        2. Переход в Личный кабинет
        3. Выход из аккаунта
        """

        main_page = MainPage(browser)
        auth_page = AuthPage(browser)

        with allure.step("Кликнуть на кнопку Личный кабинет"):
            main_page.click_personal_account_when_clickable()

        with allure.step("Кликнуть на раздел Выход"):
            auth_page.click_logout_when_clickable()

        with allure.step("Дождаться отображения кнопки 'Войти'"):
            auth_page.wait_login_when_clickable()

        with allure.step("Проверить переход на страницу Логин"):
            current_url = auth_page.verify_opened()
            assert LOGIN_URL in current_url



