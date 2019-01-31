# -*- coding: utf-8 -*-
import pytest
from model.parametrsGroup import Group
from fixture.applcation import Application


@pytest.fixture # спец. обоз. для инициал. фикстуры
def app(request):
    fixture = Application() # тут переменной fixture дали значения модуля Application, где лежат основ. сценарии
    request.addfinalizer(fixture.destroy) # вызываем функцию из Application с параметром destroy, которая завершает работу теста
    return fixture # вернем переменную



def test_test_getNewUser(app):
    app.get_url()
    app.create_acount("Boby Bush", "GBush@mail.ru")
    app.registration()
    app.add_user()
    app.add_information_about_user(Group(name="Bush", email="BushW@yahoo.com", password="11Boby_Miller1", gender="male",
                                              hobbi="writter", name_dog="milli", adress="Moscow", inn="984209854"))


"""
пояснение:
 - мы создали Фикстуру def app(request):
    - объявили переменную и передали ей значение модуля Application, где у нас хранятся все тестовые функции
    - параметру request.addfinalizer мы передали в качестве аргумента. вызов фикстуры (application.destroy())
    - и вернули результат вызова фикстуры
    
    
 - в test_test_getNewUser(app): мы передаем аргумент фиксутры (app) 
   - далее уже без параметар self мы говорим откуда брать вызов функций, а берем из аргумента app 
   - все функции вызываем из модуля Application
   
"""

