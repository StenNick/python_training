# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
import time, unittest
from parametrsGroup import Group

class test_group(unittest.TestCase):
    def setUp(self): #  функция подготовки и инициализации тестов
        self.wd = WebDriver() # запускаем драйвер тут
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)
    def get_url(self, wd):
        wd.get("http://users.bugred.ru/")
    def create_acount(self, wd, new_login, new_email):
        wd.find_element_by_xpath("//a[@href='/user/login/index.html']").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(new_login)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(new_email)
        wd.find_elements_by_name("password")[1].clear() # тут мы ищем 2й элемент из возможныз через [№index]
        wd.find_elements_by_name("password")[1].send_keys("qwerty") # тут мы ищем 2й элемент из возможныз через [№index]
    def registration(self, wd):
        wd.find_element_by_name("act_register_now").click()

    def add_user(self, wd):
        wd.find_element_by_class_name("btn-danger").click()

    def add_information_about_user(self, wd, Group):
        """
        2) тут мы хотим явно передавать переменные в функции, опять делаем рефактор
        Refactor --> Change Signature, и снимаем там галочки с параметров,
        параметры идут в вызов функции. смотри ниже
        """
        wd.find_element_by_name("noibiz_name").clear()
        wd.find_element_by_name("noibiz_name").send_keys(Group.name)
        """
        1) тут мы сделали рефакторинг кода, а именно Параметров для аргументов
        выделяем параметр в аргументе, Rafector --> Exctract --> Parametr
        и меняем название параметра, оно идет в параметры функции, где используется
        сам параметр
        """
        wd.find_element_by_name("noibiz_email").clear()
        wd.find_element_by_name("noibiz_email").send_keys(Group.email)
        wd.find_element_by_name("noibiz_password").clear()
        wd.find_element_by_name("noibiz_password").send_keys(Group.password)
        wd.find_element_by_name("noibiz_phone").clear()
        wd.find_element_by_name("noibiz_phone").send_keys("891296504605")
        wd.find_element_by_name("act_create").click()

    def test_test_getNewUser(self):
        wd = self.wd
        self.get_url(wd)
        """
        3) да да. вот тут параметры после изменения Сигнатуры, появились тут
        лучше тут их менять, т.к. это удобней читать и изменять 
        """
        self.create_acount(wd, "MnaWE", "MnaWE@mail.ru")
        time.sleep(3)
        self.registration(wd)
        time.sleep(3)
        self.add_user(wd)
        time.sleep(3)
        self.add_information_about_user(wd, Group(name="MMnaWEWer", email="AADMnaWEW@yahoo.com", password="11Boby_Robinson11", gender="male",
                                                  hobbi="writter", name_dog="milli", adress="Moscow", inn="984209854"))

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()

