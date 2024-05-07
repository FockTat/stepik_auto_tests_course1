import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


login_data = {
    'email': "andreyshishu@gmail.com",
    'password': "Andrey2024"
}


@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    'https://stepik.org/lesson/236896/step/1',
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"])
def test_login_on_stepik(browser, link):
    browser.get(link)
    wait = WebDriverWait(browser, 10)
    button = wait.until(EC.element_to_be_clickable((By.ID, "ember459")))
    button.click()
    email_field = browser.find_element(By.ID, "id_login_email")
    email_field.send_keys(login_data['email'])
    password_field = browser.find_element(By.ID, "id_login_password")
    password_field.send_keys(login_data['password'])
    btn_submit = browser.find_element(By.CSS_SELECTOR, '.button_with-loader')
    btn_submit.click()

    answer = str(math.log(int(time.time()-0.6)))
    textarea = browser.find_element(By.ID, "ember556")
    textarea.send_keys(answer)

    wait = WebDriverWait(browser, 10)
    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
    btn.click()

    correct_notification = wait.until(EC.visibility_of_element_located((By.ID, "ember543")))
    assert "Correct!" in correct_notification.text


