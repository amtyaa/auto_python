from selenium import webdriver


from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        # Конструутор, который инициализирует ссылку на драйвер и помошников
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def destroy(self):
        # Разрушает фикстуру
        self.driver.quit()

