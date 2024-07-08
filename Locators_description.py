from selenium.webdriver.common.by import By
class TestLocators:

# Кнопка "Войти в аккаунт"
    SEARCH_LOGIN_BUTTON_MAIN_PAGE = By.XPATH, ".//div[@class='BurgerConstructor_basket__container__2fUl3 mt-10']/button[text()='Войти в аккаунт']"

# Поле для ввода имени при регистрации
    SEARCH_INPUT_NAME_REGISTRATION = By.XPATH, ".//form/fieldset[1]/div/div[@class='input pr-6 pl-6 input_type_text input_size_default']/input[@class='text input__textfield text_type_main-default']"

# Поле для ввода почты при регистрации
    SEARCH_INPUT_EMAIL_REGISTRATION = By.XPATH, ".//form/fieldset[2]/div[@class='input__container']/div/input[@class='text input__textfield text_type_main-default']"

# Поле для ввода пароля при регистрации
    SEARCH_INPUT_PASSWORD_REGISTRATION = By.XPATH, ".//form/fieldset[3]/div[@class='input__container']/div/input[@class='text input__textfield text_type_main-default']"

# Кликабельная надпись для перехода к форме регистрации
    SEARCH_REGISTER_BUTTON_LOGIN_PAGE = By.XPATH, ".//div[@class='Auth_login__3hAey']/div/p[1]/a[text()='Зарегистрироваться']"

# Поле для ввода почты при входе в аккаунт
    SEARCH_INPUT_EMAIL_ACCOUNT_ENTER = By.XPATH, ".//form/fieldset[1]/div/div/input[@class='text input__textfield text_type_main-default']"

# Поле для ввода пароля при входе в аккаунт
    SEARCH_INPUT_PASSWORD_ACCOUNT_ENTER = By.XPATH, ".//form/fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default']"

# Кнопка "Войти"
    SEARCH_LOGIN_BUTTON = By.XPATH, ".//div/main/div/form/button[text()='Войти']"

# Кнопка "Зарегистрироваться"
    SEARCH_REGISTER_BUTTON = By.XPATH, ".//form/button[text()='Зарегистрироваться']"

# Текст сообщения об ошибке при вводе некорректнго пароля при регистрации
    SEARCH_INCORRECT_PASSWORD_MESSAGE = By.XPATH, ".//form/fieldset[3]/div/p[text()='Некорректный пароль']"

# Кнопка "Личный кабинет"
    SEARCH_PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//header/nav/a/p[text()='Личный Кабинет']"

# Кликабельная надпись "Войти" на экране восстановления пароля
    SEARCH_PASSWORD_RESTORATION_LOGIN_BUTTON = By.XPATH, ".//div[@class='Auth_login__3hAey']/div/p/a[text()='Войти']"

# Кликабельная надпись для восстановления пароля
    SEARCH_PASSWORD_RESTORATION_BUTTON = By.XPATH, ".//div[@class='Auth_login__3hAey']/div/p[2]/a[text()='Восстановить пароль']"

# Кликабельная надпись "Войти" на экране регистрации
    SEARCH_REGISTRATION_LOGIN_BUTTON = By.XPATH, ".//div[@class='Auth_login__3hAey']/div/p/a[text()='Войти']"

# Кнопка "Конструктор"
    SEARCH_CONSTUCTOR_BUTTON = By.XPATH, ".//header/nav/ul/li[1]/a/p[text()='Конструктор']"

# Логотип Stellar Burgers
    SEARCH_WEBSITE_LOGO = By.XPATH, ".//div[@class='App_App__aOmNj']/header/nav/div/a"

# Кнопка "Выход"
    SEARCH_LOGOUT_BUTTON = By.XPATH, ".//ul/li[3]/button[text()='Выход']"

# Неактивированный раздел "Булки"
    SEARCH_TAB_BUNS = By.XPATH, ".//section[1][@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[1]/span"

# Активированный раздел "Булки"
    SEARCH_TAB_BUNS_ACTIVE = By.XPATH, ".//main/section[1]/div[1]/div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']"

# Неактивированный раздел "Соусы"
    SEARCH_TAB_SAUCES = By.XPATH, ".//section[1][@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[2]/span"

# Активированный раздел "Соусы"
    SEARCH_TAB_SAUCES_ACTIVE = By.XPATH, ".//main/section[1]/div[1]/div[2][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']"

# Неактивированный раздел "Начинки"
    SEARCH_TAB_FILLINGS = By.XPATH, ".//section[1][@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[3]/span"

# Активированный раздел "Начинки"
    SEARCH_TAB_FILLINGS_ACTIVE = By.XPATH, ".//section[1]/div[1]/div[3][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']"
