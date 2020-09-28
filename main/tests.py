from django.test import LiveServerTestCase, TestCase, tag
from selenium import webdriver


@tag('functional')
class FunctionalTestCase(LiveServerTestCase):
    """Base class for functional test cases with selenium."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Change to another webdriver if desired (and update CI accordingly).
        chrome_options = webdriver.chrome.options.Options()
        # These options are needed for CI with Chromium.
        chrome_options.headless = True  # Disable GUI.
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        cls.selenium = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()


class MainTestCase(TestCase):
    def test_root_url_status_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class MainFunctionalTestCase(FunctionalTestCase):
    def test_root_url_exists(self):
        self.selenium.get(f'{self.live_server_url}/')
        html = self.selenium.find_element_by_tag_name('html')
        self.assertNotIn('not found', html.text.lower())
        self.assertNotIn('error', html.text.lower())
