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


def test_uncorrect_name_latin_registration():
    # Заходим на страницу регистрации
    pytest.driver.find_element("id", 'kc-register').click()
    # Вводим имя
    pytest.driver.find_element("name", 'firstName').send_keys('Ekaterina')
    # Вводим фамилию
    pytest.driver.find_element("name", 'lastName').send_keys('Ким')
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath", '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span').text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

def test_uncorrect_surname_latin_registration():
    # Заходим на страницу регистрации
    pytest.driver.find_element("id", 'kc-register').click()
    # Вводим имя
    pytest.driver.find_element("name", 'firstName').send_keys('Екатерина')
    # Вводим фамилию
    pytest.driver.find_element("name", 'lastName').send_keys('Kim')
    # Выбираем регион
    region = pytest.driver.find_element("xpath",
                                        '//div[@class="rt-input rt-input--rounded rt-input--orange rt-input--actions"]//input[@type="text"]')
    region.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    region.send_keys('Свер')
    pytest.driver.find_element("xpath", '//div[@class="rt-select__list-item"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


def test_empty_name_registration():
    # Заходим на страницу регистрации
    pytest.driver.find_element("id", 'kc-register').click()
    # Оставляем поле имени пустым
    pytest.driver.find_element("name", 'firstName').send_keys('')
    # Вводим фамилию
    pytest.driver.find_element("name", 'lastName').send_keys('Ким')
    # Выбираем регион
    region = pytest.driver.find_element("xpath",
                                        '//div[@class="rt-input rt-input--rounded rt-input--orange rt-input--actions"]//input[@type="text"]')
    region.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    region.send_keys('Свер')
    pytest.driver.find_element("xpath", '//div[@class="rt-select__list-item"]').click()
    # Вводим e-mail
    pytest.driver.find_element("id", 'address').send_keys('')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Подтверждаем пароль
    pytest.driver.find_element("id", 'password-confirm').send_keys('Dgffggh55D')
    #Жмём кнопку регистрации
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span').text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


def test_empty_surname_registration():
    # Заходим на страницу регистрации
    pytest.driver.find_element("id", 'kc-register').click()
    # Вводим имя
    pytest.driver.find_element("name", 'firstName').send_keys('Екатерина')
    # Оставляем поле фамилии пустым
    pytest.driver.find_element("name", 'lastName').send_keys('')
    # Выбираем регион
    region = pytest.driver.find_element("xpath",
                                        '//div[@class="rt-input rt-input--rounded rt-input--orange rt-input--actions"]//input[@type="text"]')
    region.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    region.send_keys('Свер')
    pytest.driver.find_element("xpath", '//div[@class="rt-select__list-item"]').click()
    # Вводим e-mail
    pytest.driver.find_element("id", 'address').send_keys('')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('')
    # Подтверждаем пароль
    pytest.driver.find_element("id", 'password-confirm').send_keys('')
    #Жмём кнопку регистрации
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


def test_just_letters_in_email_registration():
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
    # Вводим буквы вместо адреса почты и телефона
    pytest.driver.find_element("id", 'address').send_keys('вававыавы')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[3]/span').text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

def test_empty_email_registration():
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
    # Оставляем поле ввода электронной почты пустым
    pytest.driver.find_element("id", 'address').send_keys('')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Подтверждаем пароль
    pytest.driver.find_element("id", 'password-confirm').send_keys('Dgffggh55D')
    #Жмём кнопку регистрации
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[3]/span').text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

def test_wrong_numbers_phone_registration():
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
    # Вводим набор цифр
    pytest.driver.find_element("id", 'address').send_keys('435435453')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[3]/span').text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"


def test_empty_password_registration():
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
    pytest.driver.find_element("id", 'address').send_keys('') # Ввести верный email
    # Оставляем поле с паролем пустым
    pytest.driver.find_element("id", 'password').send_keys('')
    # Подтверждаем пароль
    pytest.driver.find_element("id", 'password-confirm').send_keys('Dgffggh55D')
    #Жмём кнопку регистрации
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == "Длина пароля должна быть не менее 8 символов"


def test_empty_password_confirm_registration():
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
    pytest.driver.find_element("id", 'address').send_keys('')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Оставляем поле подтверждения пароля пустым
    pytest.driver.find_element("id", 'password-confirm').send_keys('')
    #Жмём кнопку регистрации
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text == "Длина пароля должна быть не менее 8 символов"

def test_password_short_registration():
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
    pytest.driver.find_element("id", 'address').send_keys('')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('diRa4')
    # Подтверждаем пароль
    pytest.driver.find_element("id", 'password-confirm').send_keys('diRa4')
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == "Длина пароля должна быть не менее 8 символов"


def test_password_cyrillic_registration():
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
    pytest.driver.find_element("id", 'address').send_keys('')
    # Вводим пароль на кириллице
    pytest.driver.find_element("id", 'password').send_keys('куаваВыаВыа')
    # Подтверждаем пароль
    pytest.driver.find_element("id", 'password-confirm').send_keys('куаваВыаВыа')
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == "Пароль должен содержать только латинские буквы"


def test_password_without_capital_letters_registration():
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
    pytest.driver.find_element("id", 'address').send_keys('')
    # Вводим пароль без заглавных букв
    pytest.driver.find_element("id", 'password').send_keys('dfsfdsd67')
    # Подтверждаем пароль
    pytest.driver.find_element("id", 'password-confirm').send_keys('dfsfdsd67')
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == "Пароль должен содержать хотя бы одну заглавную букву"


def test_different_password_and_password_confirm_registration():
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
    pytest.driver.find_element("id", 'address').send_keys('')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Вводим в поле подтверждения пароля другой пароль
    pytest.driver.find_element("id", 'password-confirm').send_keys('Dgffggh5D')
    #Жмём кнопку регистрации
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text == "Пароли не совпадают"


def test_auth_by_uncorrect_phone():
    # Выбираем авторизацию по телефону
    pytest.driver.find_element("id", 't-btn-tab-phone').click()
    # Вводим неверный номер телефона
    pytest.driver.find_element("id", 'username').send_keys('79999999999')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Входим
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_auth_by_empty_phone():
    # Выбираем авторизацию по телефону
    pytest.driver.find_element("id", 't-btn-tab-phone').click()
    # Оставляем поле ввода телефона пустым
    pytest.driver.find_element("id", 'username').send_keys('')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Входим
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == "Введите номер телефона"

def test_auth_by_letters_in_phone():
    # Выбираем авторизацию по телефону
    pytest.driver.find_element("id", 't-btn-tab-phone').click()
    # Вводим буквы в поле ввода номера телефона
    pytest.driver.find_element("id", 'username').send_keys('ваавпвап')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Проверяем, что перенаправляет на логин
    login_button = pytest.driver.find_element("id", 't-btn-tab-login')
    # Проверяем получение сообщения об ошибке
    assert login_button.value_of_css_property('color') == 'rgba(255, 79, 18, 1)'


def test_auth_by_uncorrect_email():
    # Выбираем авторизацию по почте
    pytest.driver.find_element("id", 't-btn-tab-mail').click()
    # Вводим неверный адрес электронной почты
    pytest.driver.find_element("id", 'username').send_keys('testrostelecom555@yandex.ru')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Входим
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="form-error-message"]').text == "Неверный логин или пароль"

def test_auth_by_empty_email():
    # Выбираем авторизацию по почте
    pytest.driver.find_element("id", 't-btn-tab-mail').click()
    # Оставляем поле ввода электронной почты пустым
    pytest.driver.find_element("id", 'username').send_keys('')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Входим
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == "Введите адрес, указанный при регистрации"


def test_auth_by_letters_and_number_in_email():
    # Выбираем авторизацию по почте
    pytest.driver.find_element("id", 't-btn-tab-mail').click()
    # Вводим буквы и цифры в поле ввода электронной почты
    pytest.driver.find_element("id", 'username').send_keys('вавыа34ава')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    #Проверяем, что перенаправляет на логин
    login_button = pytest.driver.find_element("id", 't-btn-tab-login')
    assert login_button.value_of_css_property('color') == 'rgba(255, 79, 18, 1)'

def test_auth_by_uncorrect_login():
    # Выбираем авторизацию по логину
    pytest.driver.find_element("id", 't-btn-tab-login').click()
    # Вводим неверный логин
    pytest.driver.find_element("id", 'username').send_keys('Mimi555')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Входим
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="form-error-message"]').text == "Неверный логин или пароль"

def test_auth_by_empty_login():
    # Выбираем авторизацию по логину
    pytest.driver.find_element("id", 't-btn-tab-login').click()
    # Оставляем поле ввода логина пустым
    pytest.driver.find_element("id", 'username').send_keys('')
    # Вводим пароль
    pytest.driver.find_element("id", 'password').send_keys('Dgffggh55D')
    # Входим
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == "Введите логин, указанный при регистрации"


def test_auth_by_uncorrect_password():
    # Выбираем авторизацию по почте
    pytest.driver.find_element("id", 't-btn-tab-mail').click()
    # Вводим верный адрес почты
    pytest.driver.find_element("id", 'username').send_keys('')
    # Вводим неверный пароль
    pytest.driver.find_element("id", 'password').send_keys('Difdsfs44DD')
    # Входим
    pytest.driver.find_element("css selector", 'button[type="submit"]').click()
    # Проверяем получение сообщения об ошибке
    assert pytest.driver.find_element("xpath",
                                      '//*[@id="form-error-message"]').text == "Неверный логин или пароль"




