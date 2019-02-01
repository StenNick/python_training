from selenium.webdriver.chrome.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver()  # запускаем драйвер тут
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)

    def login_user(self, email, password):
        wd = self.wd
        wd.get("http://users.bugred.ru/")
        wd.find_element_by_xpath("//a[@href='/user/login/index.html']").click()
        wd.find_element_by_name("login").clear()
        wd.find_element_by_name("login").send_keys(email)
        wd.find_elements_by_name("password")[0].clear()
        wd.find_elements_by_name("password")[0].send_keys(password)
        wd.find_element_by_xpath("//input[@value='Авторизоваться']").click()


    def destroy(self):
        self.wd.quit()