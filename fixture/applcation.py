from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.create_acout import Session_registration
from fixture.login_user import Login

class Application:

    def __init__(self):
        self.wd = WebDriver()  # запускаем драйвер тут
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)
        self.session = Session_registration(self)
        self.loginUser = Login(self)

    def registration(self):
        wd = self.wd
        wd.find_element_by_name("act_register_now").click()

    def add_user(self):
        wd = self.wd
        wd.find_element_by_class_name("btn-danger").click()

    def add_information_about_user(self, Group):
        wd = self.wd
        wd.find_element_by_name("noibiz_name").clear()
        wd.find_element_by_name("noibiz_name").send_keys(Group.name)
        wd.find_element_by_name("noibiz_email").clear()
        wd.find_element_by_name("noibiz_email").send_keys(Group.email)
        wd.find_element_by_name("noibiz_password").clear()
        wd.find_element_by_name("noibiz_password").send_keys(Group.password)
        wd.find_element_by_name("noibiz_phone").clear()
        wd.find_element_by_name("noibiz_phone").send_keys("891296504605")
        wd.find_element_by_name("act_create").click()


    def destroy(self):
        self.wd.quit()