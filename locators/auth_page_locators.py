from selenium.webdriver.common.by import By


class AuthPageLocators:
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[contains(@class,'Auth_link__1fOlj')][@href='/forgot-password']")
    EMAIL_INPUT_FIELD = (By.XPATH, "//div[contains(@class, 'input_type_text')]//input[@type='text']")
    RESTORE_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Восстановить']")
    PASSWORD_TOGGLE_ICON = (By.CSS_SELECTOR, "div.input_type_password .input__icon-action svg")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "div.input_type_password")
    PASSWORD_INPUT_FIELD_ACTIVE = (By.CSS_SELECTOR, "div.input_type_text input")
    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(@class, 'Account_link__2ETsJ') and text()='История заказов']")
    LOGOUT_LINK = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")
    FIRST_ORDER_NUMBER = (By.XPATH, "(//p[@class='text text_type_digits-default'])[1]")




