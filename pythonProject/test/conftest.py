from fixture.application import Application
import pytest

@pytest.fixture
  # не смогла добавить  (scope="session")
def app(request):
  fixture = Application()
  request.addfinalizer(fixture.destroy)
  return fixture
