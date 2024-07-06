from fixture.application import Application
from model.group import Group
import pytest

@pytest.fixture
def app(request):
  fixture = Application()
  request.addfinalizer(fixture.destroy)
  return fixture


def test_addgroup(app):
    app.session.Login("admin", "secret")
    app.Creat_group(Group("sdf", "sdf", "sdf"))
    app.session.Logout()


def test_empty_addgroup(app):
    app.session.Login("admin", "secret")
    app.Creat_group(Group("","",""))
    app.session.Logout()