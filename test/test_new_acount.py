# -*- coding: utf-8 -*-
import pytest
from fixture.create_acout import SessionRegistration


@pytest.fixture # спец. обоз. для инициал. фикстуры
def app(request):
    fixture = SessionRegistration()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_new_user(app):
    app.create_acount("Anton Vodka", "Antons@mail.ru")
    app.registration()
    app.add_user()
    app.add_information(name="Anton``", email="Anton@o.com")
