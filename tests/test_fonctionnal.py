from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.core import mail

from selenium import webdriver
from users.models import User


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_argument('window-size=1200x600')

class SeleniumChromeFunctionalTestCases(StaticLiveServerTestCase):
    """Tests fonctionnels utilisant le navigateur Web GoogleChrome."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        cls.driver.implicitly_wait(30)
        #cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        super().tearDownClass()

    def setUp(self):
        User.objects.create_user(username="testuser", password="blabla12", email="jeremyguyot@orange.fr")

    def test_user_can_disconnect_and_connect(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#button-passcode').click()
        self.driver.find_element_by_css_selector('#id_email').send_keys('jeremyguyot@orange.fr')
        self.driver.find_element_by_css_selector('#button-send-reset').click()

        #logout = self.driver.find_element_by_css_selector('#button-logout')

        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Réinitialisation du mot de passe", mail.outbox[0].subject)