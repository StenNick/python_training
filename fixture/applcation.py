from selenium.webdriver.chrome.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver()  # запускаем драйвер тут
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)

    def get_url(self):
        wd = self.wd
        wd.get("http://users.bugred.ru/")
    def create_acount(self, new_login, new_email):
        wd = self.wd
        wd.find_element_by_xpath("//a[@href='/user/login/index.html']").click()
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