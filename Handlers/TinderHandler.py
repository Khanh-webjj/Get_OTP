import time
# # from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Handlers.ExcelHandler import append_to_excel
from Handlers.PhoneHandler import CallMsisonApi, CallOtpApi, call_api_continuously

PROXY = "88.209.207.107:50100"
class TestTinder():
    def setup_method(self, method):
        options = {
            'proxy': {
                'http': 'http://khanhchuoicuanam:4DVQDAJ4tZ@88.209.207.107:50100',
                'https': 'https://khanhchuoicuanam:4DVQDAJ4tZ@88.209.207.107:50100',
                'no_proxy': 'localhost,127.0.0.1'
            }
        }
        self.driver = webdriver.Chrome(seleniumwire_options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    # def test_tinder(self):
    #     self.driver.get("https://tinder.com/")
    #     self.driver.set_window_size(1936, 1096)
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Va\\(m\\):nth-child(2)"))).click()
    #
    #     wait.until(EC.element_to_be_clickable(
    #         (By.CSS_SELECTOR, ".Typs\\(body-1-strong\\) > .Typs\\(body-3-regular\\)"))).click()
    #     wait.until(EC.element_to_be_clickable(
    #         (By.CSS_SELECTOR, ".Mt\\(20px\\) .lxn9zzn"))).click()
    #     wait.until(EC.element_to_be_clickable(
    #         (By.CSS_SELECTOR, ".D\\(ib\\)--s > .Td\\(u\\)"))).click()
    #     element = wait.until(EC.element_to_be_clickable(
    #         (By.CSS_SELECTOR, ".My\\(12px\\):nth-child(3) .Mend\\(a\\)")))
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(element).perform()
    #     element.click()
    #     self.driver.find_element(By.CSS_SELECTOR, ".Bdrsbstart\\(0\\)\\!").click()
    #     self.driver.find_element(By.CSS_SELECTOR, ".Cf:nth-child(37)").click()
    #     self.driver.find_element(By.NAME, "phone_number").click()
    #     self.driver.find_element(By.NAME, "phone_number").send_keys("123456788")
    #     self.driver.find_element(By.CSS_SELECTOR, ".W\\(70\\%\\) .lxn9zzn").click()
    #     element = self.driver.find_element(By.CSS_SELECTOR, ".W\\(70\\%\\) .lxn9zzn")
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(element).perform()
    #     self.driver.switch_to.frame(8)
    #     self.driver.switch_to.frame(0)
    #     self.driver.switch_to.frame(0)
    #     self.driver.find_element(By.ID, "home_children_button").click()

    # def test_tinder(self):
    #     # Test name: Untitled
    #     # Step # | name | target | value
    #     # 1 | open | https://tinder.com/ |
    #     self.driver.get("https://tinder.com/")
    #     # 2 | setWindowSize | 778x821 |
    #     self.driver.set_window_size(778, 821)
    #     wait = WebDriverWait(self.driver, 10)
    #     # 3 | click | css=.W\(80\%\):nth-child(2) .lxn9zzn |
    #     wait.until(EC.element_to_be_clickable(
    #                (By.CSS_SELECTOR, ".W\\(80\\%\\):nth-child(2) .lxn9zzn"))).click()
    #
    #     # 4 | click | css=.D\(ib\)--s > .Td\(u\) |
    #     wait.until(EC.element_to_be_clickable(
    #         (By.CSS_SELECTOR, ".D\\(ib\\)--s > .Td\\(u\\)")))
    #     # self.driver.find_element(By.CSS_SELECTOR, ".D\\(ib\\)--s > .Td\\(u\\)").click();
    #
    #
    #     # 5 | mouseOver | css=.D\(ib\)--s > .Td\(u\) |
    #     element = self.driver.find_element(By.CSS_SELECTOR, ".D\\(ib\\)--s > .Td\\(u\\)")
    #
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(element).perform()
    #     try:
    #         element.click();
    #     except Exception as e:
    #             self.driver.set_window_size(1936, 1096)
    #             element = self.driver.find_element(By.CSS_SELECTOR, ".D\\(ib\\)--s > .Td\\(u\\)")
    #             element.click()
    #
    #
    #     # 6 | mouseOver | css=.D\(ib\)--s > .Cur\(p\) |
    #     element = self.driver.find_element(By.CSS_SELECTOR, ".D\\(ib\\)--s > .Cur\\(p\\)")
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(element).perform()
    #     # 7 | mouseOut | css=.D\(ib\)--s > .Cur\(p\) |
    #     element = self.driver.find_element(By.CSS_SELECTOR, "body")
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(element).perform()
    #     # 8 | click | css=.My\(12px\):nth-child(3) .Mend\(a\) |
    #     self.driver.find_element(By.CSS_SELECTOR, ".My\\(12px\\):nth-child(3) .Mend\\(a\\)").click()
    #
    #     # 9 | click | name=phone_number |
    #     wait.until(EC.element_to_be_clickable((By.NAME, "phone_number"))).click()
    #
    #     # 10 | type | name=phone_number | 0589072822
    #     self.driver.find_element(By.NAME, "phone_number").send_keys("589072822")
    #     # 11 | click | css=.W\(70\%\) .c9iqosj |
    #     self.driver.find_element(By.CSS_SELECTOR, ".W\\(70\\%\\) .c9iqosj").click()
    #
    #     time.sleep(60*5);
    #     # 12 | selectFrame | index=0 |
    #     # self.driver.switch_to.frame(0)
    def test_tinder(self,i,idx,workbook):
        phone = CallMsisonApi("tinder","CanTest_gw")
        print(phone['Msisdn'])
        # Test name: Untitled
        # Step # | name | target | value
        # 1 | open | https://tinder.com/ |
        self.driver.get("https://tinder.com/")
        # 2 | setWindowSize | 778x821 |
        self.driver.set_window_size(1079, 817)
        wait = WebDriverWait(self.driver, 5)
        # 3 | click |  nut "create acount"
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".Mt\(20px\) .lxn9zzn"))).click()

        # 8 | click | css=.My\(12px\):nth-child(3) .Mend\(a\) |
        time.sleep(4);
        sigUpButton = wait.until(EC.element_to_be_clickable
                                 ((By.CSS_SELECTOR, ".My\\(12px\\):nth-child(3) .Mend\\(a\\)")))
        sigUpButton.click()

        # 9 | click | name=phone_number |
        wait.until(EC.element_to_be_clickable((By.NAME, "phone_number"))).click()
        # 10 | type | name=phone_number | 0589072822
        self.driver.find_element(By.NAME, "phone_number").send_keys(phone['Msisdn'][3:])
        # 11 | click | css=.W\(70\%\) .c9iqosj |
        self.driver.find_element(By.CSS_SELECTOR, ".W\\(70\\%\\) .c9iqosj").click()
        time.sleep(4);
        mess = call_api_continuously(phone['Msisdn'],"tinder","CanTest_gw")
        append_to_excel(phone['Msisdn'],"success",mess["status"],mess['final_result'],idx,workbook)





