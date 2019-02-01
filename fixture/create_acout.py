from selenium.webdriver.chrome.webdriver import WebDriver


class SessionRegistration:

    def __init__(self):
        self.wd = WebDriver()  # запускаем драйвер тут
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)

    def create_acount(self, new_login=None, new_email=None):
        wd = self.wd
        wd.get("http://users.bugred.ru/")
        wd.find_element_by_xpath("//a[@href='/user/login/index.html']").click()
        if new_login or new_email is not None:
            wd.find_element_by_name("name").clear()
            wd.find_element_by_name("name").send_keys(new_login)
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(new_email)
        wd.find_elements_by_name("password")[1].clear() # тут мы ищем 2й элемент из возможныз через [№index]
        wd.find_elements_by_name("password")[1].send_keys("qwerty") # тут мы ищем 2й элемент из возможныз через [№index]

    def registration(self):
        wd = self.wd
        wd.find_element_by_name("act_register_now").click()

    def add_user(self):
        wd = self.wd
        wd.find_element_by_class_name("btn-danger").click()

    def add_information(self, name=None, email=None):
        wd = self.wd
        if name or email is not None:
            wd.find_element_by_name("noibiz_name").clear()
            wd.find_element_by_name("noibiz_name").send_keys(name)
            wd.find_element_by_name("noibiz_email").clear()
            wd.find_element_by_name("noibiz_email").send_keys(email)
        wd.find_element_by_name("noibiz_password").clear()
        wd.find_element_by_name("noibiz_password").send_keys("qwerty12345")
        wd.find_element_by_name("noibiz_phone").clear()
        wd.find_element_by_name("noibiz_phone").send_keys("891296504605")
        wd.find_element_by_name("act_create").click()

    def destroy(self):
        self.wd.quit()