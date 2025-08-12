import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from ..data.urls import BASE_URL
from .base_page import BasePage
from ..locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Открытие главной страницы")
    def open(self):
        self.open_url(BASE_URL)

    @allure.step("Клик на кнопку Личный кабинет")
    def click_personal_account_when_clickable(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BTN)

    @allure.step("Проверка открытия страницы")
    def verify_opened(self):
        return self.get_current_url()

    @allure.step("Клик на раздел Конструктор")
    def click_constructor_when_clickable(self):
        self.scroll_to_element(MainPageLocators.CONSTRUCTOR_LINK_ACTIVE)
        self.click_element(MainPageLocators.CONSTRUCTOR_LINK_ACTIVE)

    @allure.step("Клик на раздел Лента заказов")
    def click_order_feed_when_clickable(self):
        self.click_element(MainPageLocators.ORDER_FEED_LINK)

    @allure.step("Клик на ингридиент")
    def click_ingredient_when_clickable(self):
        self.click_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Клик на кнопку Оформить заказ")
    def click_order_registration_when_clickable(self):
        self.click_element(MainPageLocators.ORDER_REGISTRATION_BTN)

    @allure.step("Дождаться отображения модального окна")
    def wait_for_ingredient_modal_visible(self):
        """Ожидает появления модального окна с деталями ингредиента"""
        self.wait_for_element_visible(MainPageLocators.MODAL_INGREDIENT_WINDOW)
        self.wait_for_element_visible(MainPageLocators.MODAL_INGREDIENT_TITLE)
        return self

    @allure.step("Дождаться отображения модального окна заказа")
    def wait_for_order_modal_visible(self):
        """Ожидает появления модального окна оформления заказа"""
        self.wait_for_element_visible(MainPageLocators.MODAL_ORDER_WINDOW)
        self.wait_for_element_visible(MainPageLocators.MODAL_ORDER_TEXT)
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_element_text(MainPageLocators.MODAL_ORDER_NUMBER_H2) != "9999",
            message="Номер заказа не изменился"
        )
        return self

    @allure.step("Закрыть модальное окно ингридиента")
    def close_ingredient_modal(self):
        """Закрывает модальное окно с деталями ингредиента"""
        self.click_element(MainPageLocators.MODAL_INGREDIENT_CLOSE_BTN)
        self.wait_for_element_invisible(MainPageLocators.MODAL_INGREDIENT_WINDOW)
        return self

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        """Закрывает модальное окно заказа"""
        self.click_element(MainPageLocators.MODAL_ORDER_CLOSE_BTN)
        self.wait_for_element_invisible(MainPageLocators.MODAL_ORDER_WINDOW)
        return self

    @allure.step("Проверить что модальное окно ингредиента невидимо")
    def is_ingredient_modal_invisible(self, timeout=3):

        try:
            self.wait_for_element_invisible(MainPageLocators.MODAL_INGREDIENT_WINDOW, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        """Перетаскивает ингредиент в зону конструктора"""
        self.drag_and_drop_element(
            MainPageLocators.FIRST_INGREDIENT,
            MainPageLocators.CONSTRUCTOR_DROP_ZONE
        )

    @allure.step("Добавить соус в конструктор")
    def add_sauce_to_constructor(self):
        """Перетаскивает ингредиент в зону конструктора"""
        self.drag_and_drop_element(
            MainPageLocators.SAUCE_INGREDIENT,
            MainPageLocators.CONSTRUCTOR_DROP_ZONE
        )

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter_value(self):
        return int(self.get_element_text(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step("Получить значение текста окна заказа")
    def get_text_order_value(self):
        return self.get_element_text(MainPageLocators.MODAL_ORDER_TEXT)

    @allure.step("Получить номер заказа из модального окна")
    def get_number_order_value(self):
        return self.get_element_text(MainPageLocators.MODAL_ORDER_NUMBER_H2)

    @allure.step("Получить номер заказа в работе")
    def get_number_order_value_in_progress(self):
        # пауза необходима для отображения заказа
        time.sleep(1)
        return self.get_element_text(MainPageLocators.ORDER_NUMBER_IN_PROGRESS)

    @allure.step("Получить номер заказа из ленты заказов")
    def get_number_order_value_from_feed_orders(self):
        return self.get_element_text(MainPageLocators.FIRST_ORDER_NUMBER)





