from selenium.webdriver.common.by import By

class GroupHelper():
    def __init__(self, app):
        self.app = app

    def Creat(self, group):
        # Creat group
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()
        self.app.driver.find_element(By.NAME, "new").click()
        self.app.driver.find_element(By.ID, "content").click()
        self.app.driver.find_element(By.NAME, "group_name").click()
        self.app.driver.find_element(By.NAME, "group_name").send_keys(group.name_group)
        self.app.driver.find_element(By.NAME, "group_header").click()
        self.app.driver.find_element(By.NAME, "group_header").send_keys(group.header_group)
        self.app.driver.find_element(By.NAME, "group_footer").click()
        self.app.driver.find_element(By.NAME, "group_footer").send_keys(group.footer_group)
        self.app.driver.find_element(By.NAME, "submit").click()