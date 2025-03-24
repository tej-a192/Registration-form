from selenium import webdriver
from selenium.webdriver.common.by import By
import time

test_cases = [
    {
        "fullName": "User MissingPhone",
        "username": "usernopho",
        "email": "nopho@example.com",
        "phoneNumber": "",
        "password": "password123",
        "confirmPassword": "password123",
        "gender": "dot-1"
    },
    {
        "fullName": "User ShortPass",
        "username": "shortpassuser",
        "email": "shortpass@example.com",
        "phoneNumber": "9999999992",
        "password": "123",
        "confirmPassword": "123",
        "gender": "dot-2"
    },
    {
        "fullName": "Mismatch User",
        "username": "mismatchuser",
        "email": "mismatch@example.com",
        "phoneNumber": "9999999993",
        "password": "password123",
        "confirmPassword": "different123",
        "gender": "dot-3"
    },
    {
        "fullName": "Success User",
        "username": "successuser",
        "email": "success@example.com",
        "phoneNumber": "9999999994",
        "password": "validpass123",
        "confirmPassword": "validpass123",
        "gender": "dot-1"
    }
]

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")

for test in test_cases:

    driver.refresh()
    time.sleep(1)

    driver.find_element(By.ID, "fullName").send_keys(test["fullName"])
    driver.find_element(By.ID, "username").send_keys(test["username"])
    driver.find_element(By.ID, "email").send_keys(test["email"])
    driver.find_element(By.ID, "phoneNumber").send_keys(test["phoneNumber"])
    driver.find_element(By.ID, "password").send_keys(test["password"])
    driver.find_element(By.ID, "confirmPassword").send_keys(test["confirmPassword"])
    driver.find_element(By.CSS_SELECTOR, f"label[for='{test['gender']}']").click()

    driver.find_element(By.CSS_SELECTOR, ".button input").click()
    time.sleep(2)

    msg = driver.find_element(By.ID, "msg").text
    print(msg)

    time.sleep(3)

driver.quit()
