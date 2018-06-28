import os

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class HomePageTest(LiveServerTestCase):
    driver = None

    @staticmethod
    def firefox_driver():
        options = Options()
        headless = bool(int(os.environ.get('HEADLESS', 1)))
        if headless:
            options.set_headless(True)
        driver_path = os.path.join(os.environ['HOME'], 'tools', 'selenium', 'geckodriver')
        driver = webdriver.Firefox(
            firefox_options=options,
            executable_path=driver_path,
            log_path=os.path.join('logs', 'geckodriver.log')
        )
        return driver

    @staticmethod
    def chrome_driver():
        driver_path = os.path.join(os.environ['HOME'], 'tools', 'selenium', 'chromedriver')
        return webdriver.Chrome(driver_path)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = cls.firefox_driver()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        if cls.driver:
            cls.driver.quit()
            cls.driver = None

    def open(self, *args):
        url = '/'.join(args)
        self.driver.get("%s%s" % (self.live_server_url, url))

    def test_title(self):
        self.open('/')
        self.assertEqual(self.driver.title, 'Hello world')

    def test_h1(self):
        self.open('/')
        element = self.driver.find_element_by_css_selector('h1')
        self.assertEqual(element.text, 'Hello world')

