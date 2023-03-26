import pytest
import random
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def chrome_options(chrome_options):
    chrome_options.binary_location = 'c:\Chrome\chromedriver.exe'
    chrome_options.add_extension('c:\Chrome\extension.crx')
    chrome_options.add_argument('--kiosk')
    return chrome_options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('c:\Chrome\chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get("https://b2c.passport.rt.ru/")
    element = WebDriverWait(pytest.driver, 10).until(
            EC.presence_of_element_located(("id", "kc-register"))
        )

    yield

    pytest.driver.quit()


def test_correct_registration():
    # Заходим на страницу регистрации
    pytest.driver.find_element("id", 'kc-register').click()
    # Вводим имя
    pytest.driver.find_element("name", 'firstName').send_keys('Екатерина')
    # Вводим фамилию
    pytest.driver.find_element("name", 'lastName').send_keys('Ким')
    # Выбираем регион
    region = pytest.driver.find_element("xpath",
                                        '//div[@class="rt-input rt-input--rounded rt-input--orange rt-input--actions"]//input[@type="text"]')
    region.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    region.send_keys('Свер')
    pytest.driver.find_element("xpath", '//div[@class="rt-select__list-item"]').click()
    # Вводим e-mail
    random_email = random.randrange(1000000, 9999999, 1)
    pytest.driver.find_element("id", 'address').send_keys(random_email, '@test.ru')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Подтверждаем пароль
    pytest.driver.find_element("id", 'password-confirm').send_keys('Dgffggh55D')
    #Жмём кнопку регистрации
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    assert pytest.driver.find_element("tag name", 'h1').text == "Подтверждение email"

def test_correct_auth_by_email():
    # Выбираем авторизацию по телефону
    pytest.driver.find_element("id", 't-btn-tab-mail').click()
    # Вводим номер телефона
    pytest.driver.find_element("id", 'username').send_keys('') # Ввести верный email
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('')
    # Входим
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем, что оказались в личном кабинете
    assert pytest.driver.find_element("id", 'lk-btn').text == "Личный кабинет"


def test_correct_auth_by_login():
    # Выбираем авторизацию по телефону
    pytest.driver.find_element("id", 't-btn-tab-login').click()
    # Вводим верный логин
    pytest.driver.find_element("id", 'username').send_keys('')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('')
    # Входим
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем, что оказались в личном кабинете
    assert pytest.driver.find_element("id", 'lk-btn').text == "Личный кабинет"

def test_correct_agreement_page():
    # Заходим на страницу регистрации
    pytest.driver.find_element("id", 'rt-footer-agreement-link').click()

