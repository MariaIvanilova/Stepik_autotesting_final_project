import math
import time
from selenium.common.exceptions import NoAlertPresentException


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self): 
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):  # Посчитать результат математического выражения и ввести ответ
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        print(f"Your answer: {answer}")
        time.sleep(2)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            time.sleep(10)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        time.sleep(5)
