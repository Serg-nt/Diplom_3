import allure
import pytest

from ..data.test_data import counter_data, navigation_data
from ..page_objects.auth_page import AuthPage
from ..page_objects.main_page import MainPage


@allure.feature("Основной функционал")
class TestMainFunctionality:

    @pytest.mark.parametrize("test_data", navigation_data)
    @allure.title("{test_data[title]}")
    def test_navigation(self, browser, test_data):
        main_page = MainPage(browser)

        main_page.open()

        with allure.step(test_data["step_name"]):
            click_method = getattr(main_page, test_data["click_method"])
            click_method()

        with allure.step("Проверить переход на целевую страницу"):
            current_url = main_page.verify_opened()
            assert test_data["expected_url"] in current_url

    @allure.title("Детали ингредиента")
    def test_ingredient_details(self, browser):
        """
        Проверяет:
        1. Клик по ингредиенту
        2. Появление модального окна с деталями
        3. Корректность отображаемой информации
        4. Закрытие модального окна
        """
        main_page = MainPage(browser)

        main_page.open()

        with allure.step("Кликнуть на ингридиент"):
            main_page.click_ingredient_when_clickable()

        with allure.step("Дождаться открытия модального окна"):
            main_page.wait_for_ingredient_modal_visible()

        with allure.step("Закрыть модальное окно"):
            main_page.close_ingredient_modal()
            assert main_page.is_ingredient_modal_invisible(), (
                "Модальное окно должно было стать невидимым после закрытия"
            )

    @allure.title("Добавление ингредиента в заказ")
    def test_ingredient_addition(self, auth_user, browser):
        """
        Проверяет:
        1. Drag'n'drop ингредиента в конструктор
        2. Увеличение счетчика ингредиента
        3. Появление ингредиента в заказе
        """
        main_page = MainPage(browser)

        with allure.step("Запомнить начальное значение счетчика"):
            initial_count = main_page.get_ingredient_counter_value()

        with allure.step("Перетащить ингредиент в конструктор"):
            main_page.add_ingredient_to_constructor()

        with allure.step("Проверить изменение счетчика ингридиента"):
            new_count = main_page.get_ingredient_counter_value()
            assert new_count != initial_count, "Счетчик не изменился"
            assert new_count > 0, "Счетчик должен быть больше 0"

    @allure.title("Оформление заказа залогиненным пользователем")
    def test_order_registration(self, auth_user, browser):
        """
        Проверяет:
        1. Drag'n'drop ингредиента в конструктор
        2. Оформление заказа
        """
        main_page = MainPage(browser)

        with allure.step("Перетащить ингредиент в конструктор"):
            main_page.add_ingredient_to_constructor()

        with allure.step("Кликнуть на кнопку Оформить заказ"):
            main_page.click_order_registration_when_clickable()

        with allure.step("Дождаться открытия модального окна"):
            main_page.wait_for_order_modal_visible()

        assert main_page.get_text_order_value() == "Ваш заказ начали готовить"


    @allure.title("Детали заказа")
    def test_order_details(self, browser):
        """
        Проверяет:
        1. Клик по ингредиенту
        2. Появление модального окна с деталями
        3. Корректность отображаемой информации
        4. Закрытие модального окна
        """
        main_page = MainPage(browser)

        main_page.open()

        with allure.step("Кликнуть на ингридиент"):
            main_page.click_ingredient_when_clickable()

        with allure.step("Дождаться открытия модального окна"):
            main_page.wait_for_ingredient_modal_visible()

        with allure.step("Закрыть модальное окно"):
            main_page.close_ingredient_modal()
            assert main_page.is_ingredient_modal_invisible(), (
                "Модальное окно должно было стать невидимым после закрытия"
            )

    @allure.title("Проверка счетчиков")
    @pytest.mark.parametrize("locator", counter_data)
    def test_checking_counter_orders(self, auth_user, browser, locator):
        """
        Проверяет:
        1. Переход на раздел Лента Заказов
        2. Сохранение значений выполнено в переменные
        3. Оформление заказа в Конструкторе
        4. Переход в Ленту заказов
        5. Сверка значений выполнено и в работе
        """
        main_page = MainPage(browser)

        with allure.step("Кликнуть на раздел Лента заказов"):
            main_page.click_order_feed_when_clickable()

        with allure.step("Получить значение счетчика"):
            counter = main_page.get_element_text(locator)

        with allure.step("Кликнуть на раздел Конструктор"):
            main_page.click_constructor_when_clickable()

        with allure.step("Перетащить ингредиент в конструктор"):
            main_page.add_ingredient_to_constructor()

        with allure.step("Кликнуть на кнопку Оформить заказ"):
            main_page.click_order_registration_when_clickable()

        with allure.step("Дождаться открытия модального окна"):
            main_page.wait_for_order_modal_visible()

        with allure.step("Закрыть модальное окно"):
            main_page.close_order_modal()

        with allure.step("Кликнуть на раздел Лента заказов"):
            main_page.click_order_feed_when_clickable()

        with allure.step("Получить актуальное значение счетчика"):
            new_counter = main_page.get_element_text(locator)

        assert new_counter > counter

    @allure.title("Проверка отображения заказа в работе")
    def test_checking_order_in_progress(self, auth_user, browser):
        """
        Проверяет:
        1. Оформление заказа в Конструкторе
        2. Переход в Ленту заказов
        3. Сверка значений выполнено и в работе
        """
        main_page = MainPage(browser)

        with allure.step("Перетащить ингредиент в конструктор"):
            main_page.add_ingredient_to_constructor()

        with allure.step("Наполнить заказ соусами"):
            main_page.add_sauce_to_constructor()
            main_page.add_sauce_to_constructor()
            main_page.add_sauce_to_constructor()

        with allure.step("Кликнуть на кнопку Оформить заказ"):
            main_page.click_order_registration_when_clickable()

        with allure.step("Дождаться открытия модального окна"):
            main_page.wait_for_order_modal_visible()

        with allure.step("Получить номер заказа"):
            order = main_page.get_number_order_value()

        with allure.step("Закрыть модальное окно"):
            main_page.close_order_modal()

        with allure.step("Кликнуть на раздел Лента заказов"):
            main_page.click_order_feed_when_clickable()

        with allure.step("Получить актуальное значение в работе"):
            order_in_progress = main_page.get_number_order_value_in_progress()

        assert order in order_in_progress

    @allure.title("Проверка отображения заказа из Истории заказов")
    def test_checking_order_from_history_order(self, auth_user, browser):
        """
        Проверяет:
        1. Оформление заказа в Конструкторе
        2. Переход в Историю заказов
        2. Переход в Ленту заказов
        3. Сверка номера заказа из истории и ленте
        """
        main_page = MainPage(browser)
        auth_page = AuthPage(browser)

        with allure.step("Перетащить ингредиент в конструктор"):
            main_page.add_ingredient_to_constructor()

        with allure.step("Наполнить заказ соусами"):
            main_page.add_sauce_to_constructor()
            main_page.add_sauce_to_constructor()
            main_page.add_sauce_to_constructor()

        with allure.step("Кликнуть на кнопку Оформить заказ"):
            main_page.click_order_registration_when_clickable()

        with allure.step("Дождаться открытия модального окна"):
            main_page.wait_for_order_modal_visible()

        with allure.step("Закрыть модальное окно"):
            main_page.close_order_modal()

        with allure.step("Кликнуть на кнопку Личный кабинет"):
            main_page.click_personal_account_when_clickable()

        with allure.step("Кликнуть на раздел История заказов"):
            auth_page.click_order_history_when_clickable()

        with allure.step("Получить номер заказа из Истории заказов"):
            order_history = auth_page.get_number_order_value_from_history_orders()

        with allure.step("Кликнуть на раздел Лента заказов"):
            main_page.click_order_feed_when_clickable()

        with allure.step("Получить номер заказа из Ленты заказов"):
            order_feed = main_page.get_number_order_value_from_feed_orders()

        assert order_history == order_feed