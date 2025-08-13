from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BTN = (By.XPATH,
                            "//a[contains(@class,'AppHeader_header__link__3D_hX')][.//p[text()='Личный Кабинет']]")
    CONSTRUCTOR_LINK_ACTIVE = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and @href='/']")
    ORDER_FEED_LINK = (By.XPATH, "//a[@href='/feed' and .//p[text()='Лента Заказов']]")
    FIRST_INGREDIENT = (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient__1TVf6")
    SAUCE_INGREDIENT = (By.XPATH,
                        "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]//p[text()='Соус Spicy-X']/..")
    MODAL_INGREDIENT_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")
    MODAL_INGREDIENT_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_INGREDIENT_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
    CONSTRUCTOR_DROP_ZONE = (By.CSS_SELECTOR, "ul.BurgerConstructor_basket__list__l9dp_")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num__3nue1')]")
    ORDER_REGISTRATION_BTN = (By.XPATH,
                            "//button[contains(@class, 'button_button__33qZ0') and text()='Оформить заказ']")
    MODAL_ORDER_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X pt-30 pb-30')]")
    MODAL_ORDER_TEXT = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    MODAL_ORDER_NUMBER_H2 = (By.XPATH,
                             "//h2[contains(@class, 'modal__title') and contains(@class, 'text_type_digits-large')]")
    MODAL_ORDER_CLOSE_BTN = (By.XPATH,
                             "//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]")
    COUNTER_ALL_TIME = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]")
    COUNTER_TODAY = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")
    ORDER_NUMBER_IN_PROGRESS = (By.CSS_SELECTOR,
                                "ul.OrderFeed_orderListReady__1YFem li.text.text_type_digits-default")
    FIRST_ORDER_NUMBER = (By.XPATH, "(//p[@class='text text_type_digits-default'])[1]")
    OVERLAY_LOCATOR = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
