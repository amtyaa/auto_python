from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
  fixture = Application()
  request.addfinalizer(fixture.destroy)
  return fixture


def test_addcontact(app):
    app.Login("admin", "secret")
    app.Add_contact(Contact("123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123",
                     "123", "1993", "123", "123", "123", "1992", "//option[. = '14']", "//option[. = 'November']",
                     "//option[. = 'December']", "//option[. = '13']"))
    app.logout()

