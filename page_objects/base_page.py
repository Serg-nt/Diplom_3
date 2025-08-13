
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
import allure

from ..locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @allure.step("Поиск элемента {locator}")
    def search_for_element_presence(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Ожидание присутствия элемента {locator}")
    def wait_for_element_presence(self, locator):
        return self.wait.until(es.presence_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента {locator}")
    def wait_for_element_clickable(self, locator):
        self.wait.until(es.visibility_of_element_located(locator))
        return self.wait.until(es.element_to_be_clickable(locator))

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_for_element_visible(self, locator):
        return self.wait.until(es.visibility_of_element_located(locator))

    @allure.step("Ожидание скрытия элемента {locator}")
    def wait_for_element_invisible(self, locator, timeout=20):
        """Ожидает пока элемент исчезнет со страницы"""
        return WebDriverWait(self.driver, timeout).until(
            es.invisibility_of_element_located(locator),
            message=f"Элемент {locator} не исчез за {timeout} секунд"
        )

    @allure.step("Скролл к элементу {locator}")
    def scroll_to_element(self, locator):
        element = self.wait_for_element_presence(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Клик по элементу {locator}")
    def click_element(self, locator):
        try:
            self.wait_for_element_clickable(locator).click()
        except ElementClickInterceptedException as e:
            if "Modal_modal_overlay__x2ZCr" not in str(e):
                raise

            self._wait_until_overlay_disappears(MainPageLocators.OVERLAY_LOCATOR)
            self.wait_for_element_clickable(locator).click()

    def _wait_until_overlay_disappears(self, overlay_locator):
        try:
            WebDriverWait(self.driver, 5).until_not(
                es.visibility_of_element_located(overlay_locator)
            )
        except TimeoutException:
            pass

    @allure.step("Ввод текста '{text}' в элемент {locator}")
    def send_keys_to_element(self, locator, text):
        self.wait_for_element_visible(locator).send_keys(text)

    @allure.step("Получение текста элемента {locator}")
    def get_element_text(self, locator):
        return self.wait_for_element_visible(locator).text

    @allure.step("Открытие URL: {url}")
    def open_url(self, url: str):
        self.driver.get(url)

    @allure.step("Получение текущего URL")
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Проверка соответствия URL ожидаемому: {expected_url}")
    def is_current_url_matches(self, expected_url: str) -> bool:
        return self.get_current_url() == expected_url

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            es.visibility_of_element_located(locator),
            message=f"Элемент {locator} не стал видимым за {timeout} секунд"
        )

    @allure.step("Проверить видимость элемента {locator}")
    def is_visible(self, locator, timeout=10) -> bool:
        try:
            self.wait_for_element_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step('Drag and Drop an element')
    def drag_and_drop_element(self, locator_from, locator_to):
        self.is_visible(locator_from)
        self.is_visible(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            """, element_from, element_to)

    @allure.step("Ожидание условия с таймаутом")
    def wait_for_condition(self, condition, timeout=10, message=""):
        return WebDriverWait(self.driver, timeout).until(
            condition,
            message=message if message else f"Условие не выполнено за {timeout} секунд"
        )