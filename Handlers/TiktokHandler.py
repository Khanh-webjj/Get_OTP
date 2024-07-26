import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import  Proxy, ProxyType


class TestTiktok():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_tiktok(self):
        self.driver.get("https://www.tiktok.com/login/phone-or-email")
        self.driver.set_window_size(1066, 758)
        self.driver.find_element(By.CSS_SELECTOR, ".tiktok-so52kr-StyledArrowIcon > path").click()
        self.driver.find_element(By.ID, "login-phone-search").send_keys("855")
        self.driver.find_element(By.ID, "KH-855").click()
        self.driver.find_element(By.NAME, "mobile").click()
        self.driver.find_element(By.NAME, "mobile").send_keys("182548177")
        self.driver.find_element(By.CSS_SELECTOR, ".tiktok-1jjb4td-ButtonSendCode").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".tiktok-1jjb4td-ButtonSendCode")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".tiktok-1jjb4td-ButtonSendCode").click()
        time.sleep(10)
