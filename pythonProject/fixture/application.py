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

    def Add_contact(self, contact):
        # Add new contact
        self.driver.find_element(By.LINK_TEXT, "add new").click()
        self.driver.find_element(By.NAME, "firstname").click()
        self.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        self.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.driver.find_element(By.NAME, "title").send_keys(contact.title)
        self.driver.find_element(By.NAME, "company").send_keys(contact.company)
        self.driver.find_element(By.NAME, "address").send_keys(contact.address)
        self.driver.find_element(By.NAME, "home").send_keys(contact.home)
        self.driver.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        self.driver.find_element(By.NAME, "work").send_keys(contact.work)
        self.driver.find_element(By.NAME, "fax").send_keys(contact.fax)
        self.driver.find_element(By.NAME, "email").send_keys(contact.email)
        self.driver.find_element(By.NAME, "email2").send_keys(contact.email2)
        self.driver.find_element(By.NAME, "email3").send_keys(contact.email3)
        self.driver.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        self.driver.find_element(By.NAME, "bday").click()
        dropdown = self.driver.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, contact.bday1).click()
        self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(16)").click()
        dropdown = self.driver.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, contact.bmonth1).click()
        self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(12)").click()
        self.driver.find_element(By.NAME, "byear").send_keys(contact.byear1)
        self.driver.find_element(By.NAME, "aday").click()
        dropdown = self.driver.find_element(By.NAME, "aday")
        dropdown.find_element(By.XPATH, contact.aday2).click()
        self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(15)").click()
        self.driver.find_element(By.NAME, "amonth").click()
        dropdown = self.driver.find_element(By.NAME, "amonth")
        dropdown.find_element(By.XPATH, contact.amonth2).click()
        self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(13)").click()
        self.driver.find_element(By.NAME, "ayear").send_keys(contact.ayear2)
        self.driver.find_element(By.NAME, "address2").click()
        self.driver.find_element(By.NAME, "address2").send_keys(contact.address2)
        self.driver.find_element(By.NAME, "phone2").click()
        self.driver.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        self.driver.find_element(By.NAME, "notes").click()
        self.driver.find_element(By.NAME, "notes").send_keys(contact.notes)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()

