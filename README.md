Тесты и их вызов:
1. Корректная регистрация на сайте при верных данных. Запуск теста: python -m pytest test_rostelecom_positive.py::test_correct_registration 
2. Корректность авторизации по электронной почте и паролю. Запуск теста: python -m pytest test_rostelecom_positive.py::test_correct_auth_by_email 
3. Корректность авторизации по логину и паролю. Запуск теста: python -m pytest test_rostelecom_positive.py::test_correct_auth_by_login
4. Сообщение об ошибке при авторизации по некорректному номеру телефона. Запуск теста: python -m pytest test_rostelecom_negative.py::test_auth_by_uncorrect_phone 
5. Сообщение об ошибке при авторизации с пустым полем номера телефона. Запуск теста: python -m pytest test_rostelecom_negative.py::test_auth_by_empty_phone 
6. Сообщение об ошибке при авторизации по некорректному адресу электронной почты. Запуск теста: python -m pytest test_rostelecom_negative.py::test_auth_by_uncorrect_email 
7. Сообщение об ошибке при авторизации с пустым полем электронной почты. Запуск теста: python -m pytest test_rostelecom_negative.py::test_auth_by_empty_email 
8. Сообщение об ошибке при авторизации по некорректному логину. Запуск теста: python -m pytest test_rostelecom_negative.py::test_auth_by_uncorrect_login 
9. Сообщение об ошибке при авторизации с пустым полем логина. Запуск теста: python -m pytest test_rostelecom_negative.py::test_auth_by_empty_login 
10. Сообщение об ошибке при авторизации при некорректном пароле. Запуск теста: python -m pytest test_rostelecom_negative.py::test_auth_by_uncorrect_password 
11. Сообщение об ошибке при авторизации при вводе в поле номера телефона букв. Запуск теста: python -m pytest test_rostelecom_negative.py::test_auth_by_letters_in_phone 
12. Сообщение об ошибке при авторизации при вводе в поле электронной почты набора из букв и цифр. Запуск теста: python -m pytest test_rostelecom_negative.py::test_auth_by_letters_and_number_in_email 
13. Сообщение об ошибке при регистрации при вводе имени латинскими буквами. Запуск теста: python -m pytest test_rostelecom_negative.py::test_uncorrect_name_latin_registration 
14. Сообщение об ошибке при регистрации при пустом поле ввода имени. Запуск теста: python -m pytest test_rostelecom_negative.py::test_empty_name_registration 
15. Сообщение об ошибке при регистрации при вводе фамилии латинскими буквами. Запуск теста: python -m pytest test_rostelecom_negative.py::test_uncorrect_surname_latin_registration 
16. Сообщение об ошибке при регистрации при пустом поле ввода фамилии. Запуск теста: python -m pytest test_rostelecom_negative.py::test_empty_surname_registration 
17. Сообщение об ошибке при регистрации при вводе набора букв в поле ввода электронной почты/телефона. Запуск теста: python -m pytest test_rostelecom_negative.py::test_just_letters_in_email_registration 
18. Сообщение об ошибке при регистрации при пустом поле ввода электронной почты/телефона. Запуск теста: python -m pytest test_rostelecom_negative.py::test_empty_email_registration
19. Сообщение об ошибке при регистрации при вводе набора цифр в поле ввода электронной почты/телефона. Запуск теста: python -m pytest test_rostelecom_negative.py::test_wrong_numbers_phone_registration 
20. Сообщение об ошибке при регистрации при пустом поле ввода пароля. Запуск теста: python -m pytest test_rostelecom_negative.py::test_empty_password_registration 
21. Сообщение об ошибке при регистрации при пустом поле ввода подтверждения пароля. Запуск теста: python -m pytest test_rostelecom_negative.py::test_empty_password_confirm_registration 
22. Сообщение об ошибке при регистрации при вводе пароля менее 8 символов. Запуск теста: python -m pytest test_rostelecom_negative.py::test_password_short_registration 
23. Сообщение об ошибке при регистрации при вводе пароля кириллицей. Запуск теста: python -m pytest test_rostelecom_negative.py::test_password_cyrillic_registration 
24. Сообщение об ошибке при регистрации при вводе пароля без заглавных букв. Запуск теста: python -m pytest test_rostelecom_negative.py::test_password_without_capital_letters_registration 
25. Сообщение об ошибке при регистрации при разных паролях в поле "Пароль" и "Подтверждение пароля". Запуск теста: python -m pytest test_rostelecom_negative.py::test_different_password_and_password_confirm_registration 
26. Открытие страницы с пользовательским соглашением при нажатии ссылки в футере "Политикой конфиденциальности и Пользовательским соглашением" в футере. Запуск теста: python -m pytest test_rostelecom_positive.py::test_correct_agreement_page 
