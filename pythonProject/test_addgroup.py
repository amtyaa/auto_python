from application import Application
from group import Group
import pytest

@pytest.fixture
def app(request):
  fixture = Application()
  request.addfinalizer(fixture.destroy)
  return fixture


def test_addgroup(app):
    app.Login("admin", "secret")
    app.Creat_group(Group("sdf", "sdf", "sdf"))
    app.logout()


def test_empty_addgroup(app):
    app.Login("admin", "secret")
    app.Creat_group(Group("","",""))
    app.logout()