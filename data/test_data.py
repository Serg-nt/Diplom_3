from .urls import BASE_URL, ORDER_FEED_URL
from ..locators.main_page_locators import MainPageLocators

counter_data = [
    MainPageLocators.COUNTER_ALL_TIME,
    MainPageLocators.COUNTER_TODAY,
]

navigation_data = [
        {
            "title": "Переход в Конструктор",
            "step_name": "Кликнуть на раздел Конструктор",
            "click_method": "click_constructor_when_clickable",
            "expected_url": BASE_URL,
        },
        {
            "title": "Переход в Ленту заказов",
            "step_name": "Кликнуть на раздел Лента заказов",
            "click_method": "click_order_feed_when_clickable",
            "expected_url": ORDER_FEED_URL,
        }
    ]