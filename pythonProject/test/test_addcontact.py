from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
  fixture = Application()
  request.addfinalizer(fixture.destroy)
  return fixture


def test_addcontact(app):
    app.session.Login("admin", "secret")
    app.contact.Add(Contact("123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123",
                     "123", "1993", "123", "123", "123", "1992", "//option[. = '14']", "//option[. = 'November']",
                     "//option[. = 'December']", "//option[. = '13']"))
    app.session.Logout()

