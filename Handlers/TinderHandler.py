import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTinder():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()


    def test_tinder(self):
        # Step # | name | target | value
        # 1 | open | https://tinder.com/ |
        self.driver.get("https://tinder.com/")
        # 2 | setWindowSize | 778x821 |
        self.driver.set_window_size(1079,817)
        wait = WebDriverWait(self.driver, 10)
        # 3 | click |  nut "create acount"
        wait.until(EC.element_to_be_clickable(
                   (By.CSS_SELECTOR, ".Mt\(20px\) .lxn9zzn"))).click()

        # 8 | click | css=.My\(12px\):nth-child(3) .Mend\(a\) |
        time.sleep(1);
        sigUpButton = self.driver.find_element(By.CSS_SELECTOR, ".My\\(12px\\):nth-child(3) .Mend\\(a\\)")
        sigUpButton.click()

        # 9 | click | name=phone_number |
        wait.until(EC.element_to_be_clickable((By.NAME, "phone_number"))).click()
        # 10 | type | name=phone_number | 0589072822
        self.driver.find_element(By.NAME, "phone_number").send_keys("589072822")
        # 11 | click | css=.W\(70\%\) .c9iqosj |
        self.driver.find_element(By.CSS_SELECTOR, ".W\\(70\\%\\) .c9iqosj").click()
        if self.CaptchaExist():
            wait.until(EC.element_to_be_clickable((By.ID, "home_children_button"))).click()
        time.sleep(60*5)

    def CaptchaExist(self):
        print("captchaExistCheck")
        try:
            time.sleep(5)
            # WebDriverWait(self.driver, 20).until(
            #     EC.presence_of_element_located((By.ID, "home")))
            self.driver.find_element(By.ID, "home")

        except:
            print("cant find verify capcha")
            return False
        return True

