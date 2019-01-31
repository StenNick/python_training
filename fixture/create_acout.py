
class Session_registration():

    def __init__(self, app):
        self.app = app

    def create_new_acount(self, new_login, new_email):
        wd = self.app.wd
        wd.get("http://users.bugred.ru/")
        wd.find_element_by_xpath("//a[@href='/user/login/index.html']").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(new_login)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(new_email)
        wd.find_elements_by_name("password")[1].clear() # тут мы ищем 2й элемент из возможныз через [№index]
        wd.find_elements_by_name("password")[1].send_keys("qwerty") # тут мы ищем 2й элемент из возможныз через [№index]