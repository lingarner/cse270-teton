# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


class TestSmokeTest2():
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_spotlightTest(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
        self.driver.set_window_size(1936, 1168)
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, ".spotlight1 > .centered-image")
        assert len(elements) > 0
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, ".spotlight2 > .centered-image")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.LINK_TEXT, "Join Us")
        assert len(elements) > 0
        self.driver.find_element(By.LINK_TEXT, "Join Us").click()
        assert self.driver.find_element(
            By.CSS_SELECTOR, "section > h3").text == "Welcome to the Teton Chamber of Commerce Signup Wizard!"

    def test_nameandLogoTest(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
        self.driver.set_window_size(1936, 1168)
        assert self.driver.title == "Teton Idaho CoC"
        assert self.driver.find_element(
            By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
        assert self.driver.find_element(
            By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, ".header-logo img")
        assert len(elements) > 0

    def test_joinPageTest(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/join.html")
        self.driver.set_window_size(1936, 1168)
        assert self.driver.find_element(
            By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "First Name"
        elements = self.driver.find_elements(By.NAME, "fname")
        assert len(elements) > 0
        self.driver.find_element(By.NAME, "fname").send_keys("Lidnsay")
        self.driver.find_element(By.NAME, "lname").send_keys("Garner")
        self.driver.find_element(By.NAME, "bizname").send_keys("help")
        self.driver.find_element(By.NAME, "biztitle").send_keys("ceo")
        self.driver.find_element(By.NAME, "submit").click()
        assert self.driver.find_element(
            By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Email"
        elements = self.driver.find_elements(By.NAME, "email")
        assert len(elements) > 0

    def test_directoryTest(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/directory.html")
        self.driver.set_window_size(1936, 1168)
        self.driver.find_element(
            By.CSS_SELECTOR, "section:nth-child(2)").click()
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
        assert len(elements) > 0
        assert self.driver.find_element(
            By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
        self.driver.find_element(By.ID, "directory-list").click()
        assert self.driver.find_element(
            By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
        assert len(elements) > 0

    def test_adminPageTest(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/admin.html")
        self.driver.set_window_size(1936, 1168)
        assert self.driver.find_element(
            By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Username:"
        elements = self.driver.find_elements(By.ID, "username")
        assert len(elements) > 0
        self.driver.find_element(By.ID, "username").send_keys("incorrect")
        self.driver.find_element(By.ID, "password").send_keys("badpassword")
        self.driver.find_element(
            By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".errorMessage")
        assert len(elements) > 0
        self.driver.find_element(
            By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
