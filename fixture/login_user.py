import time

class Login():
    def __init__(self, app):
        self.app = app

    def login_user(self, email, password):
        wd = self.app.wd
        wd.get("http://users.bugred.ru/")
        time.sleep(1)
        wd.find_element_by_xpath("//a[@href='/user/login/index.html']").click()
        time.sleep(2)
        wd.find_element_by_name("login").clear()
        wd.find_element_by_name("login").send_keys(email)
        time.sleep(2)
        wd.find_elements_by_name("password")[0].clear()
        wd.find_elements_by_name("password")[0].send_keys(password)
        time.sleep(2)
        wd.find_element_by_xpath("//input[@value='Авторизоваться']").click()
        time.sleep(2)

# time sleep() не следует использовать, он тут создан для наглядности, что бы проверить заполнение полей 