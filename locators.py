from selenium.webdriver.common.by import By
class TestLocators:

# Кнопка "Войти в аккаунт"
    SEARCH_LOGIN_BUTTON_MAIN_PAGE = By.XPATH, ".//button[text()='Войти в аккаунт']"

# Поле для ввода имени при регистрации
    SEARCH_INPUT_NAME_REGISTRATION = By.XPATH, "(.//input[@name='name' and @type='text'])[1]"

# Поле для ввода почты при регистрации
    SEARCH_INPUT_EMAIL_REGISTRATION = By.XPATH, "(//input[@name='name' and @type='text'])[2]"

# Поле для ввода пароля при регистрации
    SEARCH_INPUT_PASSWORD_REGISTRATION = By.XPATH, "//input[@type='password']"

# Кликабельная надпись для перехода к форме регистрации
    SEARCH_REGISTER_BUTTON_LOGIN_PAGE = By.XPATH, ".//a[@class='Auth_link__1fOlj' and @href='/register']"

# Поле для ввода почты при входе в аккаунт
    SEARCH_INPUT_EMAIL_ACCOUNT_ENTER = By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='text' and @name='name']"

# Поле для ввода пароля при входе в аккаунт
    SEARCH_INPUT_PASSWORD_ACCOUNT_ENTER = By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='password' and @name='Пароль']"

# Кнопка "Войти"
    SEARCH_LOGIN_BUTTON = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Войти']"

# Кнопка "Зарегистрироваться"
    SEARCH_REGISTER_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Зарегистрироваться']"

# Текст сообщения об ошибке при вводе некорректнго пароля при регистрации
    SEARCH_INCORRECT_PASSWORD_MESSAGE = By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']"

# Кнопка "Личный кабинет"
    SEARCH_PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']"

# Кликабельная надпись "Войти" на экране восстановления пароля
    SEARCH_PASSWORD_RESTORATION_LOGIN_BUTTON = By.XPATH, ".//a[@class='Auth_link__1fOlj' and @href='/login']"

# Кликабельная надпись для восстановления пароля
    SEARCH_PASSWORD_RESTORATION_BUTTON = By.XPATH, ".//a[@class='Auth_link__1fOlj' and @href='/forgot-password']"

# Кликабельная надпись "Войти" на экране регистрации
    SEARCH_REGISTRATION_LOGIN_BUTTON = By.XPATH, ".//a[@class='Auth_link__1fOlj' and @href='/login']"

# Кнопка "Конструктор"
    SEARCH_CONSTUCTOR_BUTTON = By.XPATH, ".//p[text()='Конструктор']"

# Логотип Stellar Burgers
    SEARCH_WEBSITE_LOGO = By.XPATH, ".//a[@href='/']"

# Кнопка "Выход"
    SEARCH_LOGOUT_BUTTON = By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"

# Неактивированный раздел "Булки"
    SEARCH_TAB_BUNS = By.XPATH, ("//div[contains(@class, 'tab_tab__1SPyG') and .//span[@class='text text_type_main-default' and text()='Булки']]")

# Активированный раздел "Булки"
    SEARCH_TAB_BUNS_ACTIVE = By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Булки']"

# Неактивированный раздел "Соусы"
    SEARCH_TAB_SAUCES = By.XPATH, ("//div[contains(@class, 'tab_tab__1SPyG') and .//span[@class='text text_type_main-default' and text()='Соусы']]")

# Активированный раздел "Соусы"
    SEARCH_TAB_SAUCES_ACTIVE = By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Соусы']"

# Неактивированный раздел "Начинки"
    SEARCH_TAB_FILLINGS = By.XPATH, ("//div[contains(@class, 'tab_tab__1SPyG') and .//span[@class='text text_type_main-default' and text()='Начинки']]")

# Активированный раздел "Начинки"
    SEARCH_TAB_FILLINGS_ACTIVE = By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Начинки']"
