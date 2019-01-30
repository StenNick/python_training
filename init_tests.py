# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
from parametrsGroup import Group
from applcation import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

class test_group(unittest.TestCase):
    def setUp(self):
        self.app = Application
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)

    def test_test_getNewUser(self):
        wd = self.wd
        self.app.get_url(wd)
        self.app.create_acount("Milena", "MilenaE@mail.ru")
        time.sleep(3)
        self.app.registration()
        time.sleep(3)
        self.app.add_user()
        time.sleep(3)
        self.app.add_information_about_user(Group(name="Milena22aq", email="Milena111W@yahoo.com", password="11Boby_Robinson11", gender="male",
                                                  hobbi="writter", name_dog="milli", adress="Moscow", inn="984209854"))
    def tearDown(self):
        self.app.destroy()


if __name__ == '__main__':
    unittest.main()

