import math
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
#
#
# link = 'http://suninjuly.github.io/find_xpath_form'
# # what_search = 'layout__topbar_add-question'
#
# # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# try:
#     browser = webdriver.Chrome()
# # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
#     browser.get(link)
#
#     # elements = browser.find_elements(By.CSS_SELECTOR,"input[type='text']")
#     # for element in elements:
#     #     element.send_keys("Мой ответ")
#
#     # button = browser.find_element(By.XPATH, "button[type='submit']")
#     # button.click()
#
#     # link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
#     # link.click()
#
#     # link = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
#     # link.click()
#     #
#     input1 = browser.find_element(By.TAG_NAME, 'input')
#     input1.send_keys("Andrey")
#
#     input2 = browser.find_element(By.NAME, 'last_name')
#     input2.send_keys("Petrov")
#
#     input3 = browser.find_element(By.CLASS_NAME, 'city')
#     input3.send_keys("Smolensk")
#
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     #
#     # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     # button.click()
#     button = browser.find_element(By.XPATH, "//button[@type='submit']")
#     button.click()
# #
# # browser.find_element(By.CLASS_NAME, what_search).click()
# #
# # browser.find_element(By.CSS_SELECTOR, 'li[class="filters-menu__item"]').click()
#
# # Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# # Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# # Ищем поле для ввода текста
# # browser.find_element(By.XPATH, '//*[@id="js-canvas"]/div[1]/div/div/div/div[3]/nav/ul/li[3]').click()
# # browser.find_element(By.XPATH,'//*[@id="js-canvas"]/div[1]/div/div/div/div[4]/ul[1]/li[1]/div/div[1]/div/h2').click()
# # browser.find_element(By.XPATH, '//*[@id="question_show"]/div[1]/div[3]/div/img[1]').click()
# #
# # link = browser.find_element(By.LINK_TEXT, 'Как сделать скриншот или запись, если запрещено?')
# # link.click()
#
# # get_start = browser.find_element(By.LINK_TEXT, 'Какие книги посоветуете по нейросетям?').click()
#
# # После выполнения всех действий мы должны не забыть закрыть окно браузера
# finally:
#     # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
#     sleep(30)
#     browser.quit()


# тест окошка регистрации
# try:
#     link = "http://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control')
#     input1.send_keys("Andrey")
#
#     elements = browser.find_elements(By.CSS_SELECTOR, 'input[required]')
#     for element in elements:
#         element.send_keys("Test text")
#
#
#
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# тест чекбокса и радиокнопок
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     link = "http://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element(By.ID, "treasure")
#     x = x_element.get_attribute("valuex")
#     y = calc(x)
#
#     input1 = browser.find_element(By.ID, 'answer')
#     input1.send_keys(y)
#
#     Checkbox = browser.find_element(By.ID, 'robotCheckbox')
#     Checkbox.click()
#
#     radio = browser.find_element(By.ID, "robotsRule")
#     radio.click()
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# раскрывающийся список

# link = "https://suninjuly.github.io/selects1.html"
# browser = webdriver.Chrome()
# browser.get(link)
# try:
#     a = browser.find_element(By.ID, "num1").text # извлекли из элемента конкретно то что он содержит. (.text - это по дефолту СТРОКА)
#     b = browser.find_element(By.ID, "num2").text
#     result = str((int(a) + int(b))) # Строки превращаем в числа int(a) , int(b) и складываем!. Но тк мы должны выбрать далее элемент для сравнения . конечное число преобразуем в строку
#     Select(browser.find_element(By.CLASS_NAME, "custom-select")).select_by_value(result) # а вот тут преобр.строку отдаем на поиск в браузере
#     browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
#
# finally:
#     time.sleep(5)

# скролл страницы вниз, если закрывает кнопку футер
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     y = calc(x)
#
#     browser.execute_script("window.scrollBy(0, 100);")
#
#     input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control")
#     input1.send_keys(y)
#
#     Checkbox = browser.find_element(By.ID, 'robotCheckbox')
#     Checkbox.click()
#
#     radio = browser.find_element(By.ID, "robotsRule")
#     radio.click()
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#
# finally:
#     time.sleep(10)


# работа с файлами
# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/file_input.html"
# browser.get(link)
#
# try:
#     input_first = browser.find_element(By.NAME, 'firstname')
#     input_first.send_keys('Andrey')
#
#     input_last = browser.find_element(By.NAME, 'lastname')
#     input_last.send_keys('Shishu')
#
#     input_email = browser.find_element(By.NAME, 'email')
#     input_email.send_keys('asdad@ffsd.ru')
#
#     current_dir = os.path.abspath(os.path.dirname('selen_course.py'))    # получаем путь к директории текущего исполняемого файла
#     print(current_dir)
#     file = 'file.txt'  # имя файла, который будем загружать на сайт
#     file_path = os.path.join(current_dir, file)  # добавляем к этому пути имя файла
#
#     element = browser.find_element(By.ID, "file")
#     element.send_keys(file_path)
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
# finally:
#     time.sleep(10)


# работа с alert
# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/alert_accept.html"
# browser.get(link)
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
# try:
#     button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
#     button.click()
#
#     confirm = browser.switch_to.alert
#     confirm.accept()
#
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     y = calc(x)
#
#     input1 = browser.find_element(By.ID, 'answer')
#     input1.send_keys(y)
#
#     btn = browser.find_element(By.XPATH, '//button[@type="submit"]')
#     btn.click()
#
# finally:
#     time.sleep(10)


# переход на другую страницу

# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/redirect_accept.html"
# browser.get(link)
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
# try:
#     btn = browser.find_element(By.XPATH, '//button[@type="submit"]')
#     btn.click()
#
#     new_windows = browser.window_handles[1]
#     browser.switch_to.window(new_windows)
#
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     y = calc(x)
#
#     input1 = browser.find_element(By.ID, 'answer')
#     input1.send_keys(y)
#
#     btn2 = browser.find_element(By.XPATH, '//button[@type="submit"]')
#     btn2.click()
# finally:
#     time.sleep(10)

# metod get

# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     # говорим WebDriver искать каждый элемент в течение 5 секунд
#     browser.implicitly_wait(5)
#
#     browser.get("http://suninjuly.github.io/explicit_wait2.html")
#
#     # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#     element = WebDriverWait(browser, 12).until(
#             EC.text_to_be_present_in_element((By.ID, "price"), '$100')
#         )
#     btn = browser.find_element(By.ID, 'book')
#     btn.click()
#
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     y = calc(x)
#
#     input1 = browser.find_element(By.ID, 'answer')
#     input1.send_keys(y)
#
#     btn2 = browser.find_element(By.XPATH, '//button[@type="submit"]')
#     btn2.click()
# finally:
#     time.sleep(5)

numbers = [1, 2, 3, 4, 5, 6, 1, 7, 5, 45]
result = set(numbers)
print(result)