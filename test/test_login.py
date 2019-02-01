# -*- coding: utf-8 -*-
import pytest
from fixture.applcation import Application


@pytest.fixture # спец. обоз. для инициал. фикстуры
def app(request):
    fixture = Application() # тут переменной fixture дали значения модуля Application, где лежат основ. сценарии
    request.addfinalizer(fixture.destroy) # вызываем функцию из Application с параметром destroy, которая завершает работу теста
    return fixture # вернем переменную


def test_login_user(app):
    app.login_user("AlexBold@mail.ruuuus", "12345")



