from selenium.webdriver.common.by import By
class SessionHelper():
    def __init__(self, app):
        self.app = app

    def Logout(self):
        # Logout
        self.app.driver.find_element(By.LINK_TEXT, "Logout").click()

    def Login(self, username, password):
        # Login
        self.app.driver.get("http://localhost/addressbook/")
        self.app.driver.find_element(By.NAME, "user").click()
        self.app.driver.find_element(By.NAME, "user").send_keys(username)
        self.app.driver.find_element(By.NAME, "pass").click()
        self.app.driver.find_element(By.NAME, "pass").send_keys(password)
        self.app.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()