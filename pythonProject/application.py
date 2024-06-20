from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def destroy(self):
        self.driver.quit()

    def logout(self):
        # Logout
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def Creat_group(self, group):
        # Creat group
        self.driver.find_element(By.LINK_TEXT, "groups").click()
        self.driver.find_element(By.NAME, "new").click()
        self.driver.find_element(By.ID, "content").click()
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name_group)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header_group)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer_group)
        self.driver.find_element(By.NAME, "submit").click()


    def Login(self, username, password):
        # Login
        self.driver.get("http://localhost/addressbook/")
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").click()
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()




