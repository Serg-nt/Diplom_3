import allure

from ..locators.auth_page_locators import AuthPageLocators
from .base_page import BasePage


class AuthPage(BasePage):

    @allure.step("Клик на ссылку Восстановить пароль")
    def click_restore_password_link(self):
        self.click_element(AuthPageLocators.RESTORE_PASSWORD_LINK)

    @allure.step("Введение корректной почты")
    def enter_email(self, email):
        self.send_keys_to_element(AuthPageLocators.EMAIL_INPUT_FIELD, email)

    @allure.step("Клик на кнопку Восстановить")
    def click_restore_button(self):
        self.click_element(AuthPageLocators.RESTORE_BUTTON)

    @allure.step("Клик на ссылку История заказов")
    def click_order_history_when_clickable(self):
        self.click_element(AuthPageLocators.ORDER_HISTORY_LINK)

    @allure.step("Клик на ссылку Выход")
    def click_logout_when_clickable(self):
        self.click_element(AuthPageLocators.LOGOUT_LINK)

    @allure.step("Ожидание кнопки Войти")
    def wait_login_when_clickable(self):
        self.wait_for_element_clickable(AuthPageLocators.LOGIN_BUTTON)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.send_keys_to_element(AuthPageLocators.PASSWORD_INPUT_FIELD, password)

    @allure.step("Клик на кнопку 'Войти'")
    def click_login_button(self):
        self.click_element(AuthPageLocators.LOGIN_BUTTON)

    @allure.step("Клик по иконке глаза для показа/скрытия пароля")
    def click_password_toggle_icon(self):
        self.click_element(AuthPageLocators.PASSWORD_TOGGLE_ICON)

    @allure.step("Проверить видимость пароля")
    def is_password_visible(self) -> bool:
        """Проверяет, что тип поля изменился на 'text'"""
        field = self.driver.find_element(*AuthPageLocators.PASSWORD_INPUT_FIELD_ACTIVE)
        return field.get_attribute("type") == "text"

    @allure.step("Проверка открытия страницы")
    def verify_opened(self):
        return self.get_current_url()

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        """Выполняет авторизацию пользователя."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()


    @allure.step("Получить номер заказа из истории заказов")
    def get_number_order_value_from_history_orders(self):
        return self.get_element_text(AuthPageLocators.FIRST_ORDER_NUMBER)

