from selenium.webdriver.common.by import By

class ContactHelper():
    def __init__(self, app):
        self.app = app

    def Add(self, contact):
        # Add new contact
        self.app.driver.find_element(By.LINK_TEXT, "add new").click()
        self.app.driver.find_element(By.NAME, "firstname").click()
        self.app.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.app.driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        self.app.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.app.driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.app.driver.find_element(By.NAME, "title").send_keys(contact.title)
        self.app.driver.find_element(By.NAME, "company").send_keys(contact.company)
        self.app.driver.find_element(By.NAME, "address").send_keys(contact.address)
        self.app.driver.find_element(By.NAME, "home").send_keys(contact.home)
        self.app.driver.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        self.app.driver.find_element(By.NAME, "work").send_keys(contact.work)
        self.app.driver.find_element(By.NAME, "fax").send_keys(contact.fax)
        self.app.driver.find_element(By.NAME, "email").send_keys(contact.email)
        self.app.driver.find_element(By.NAME, "email2").send_keys(contact.email2)
        self.app.driver.find_element(By.NAME, "email3").send_keys(contact.email3)
        self.app.driver.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        self.app.driver.find_element(By.NAME, "bday").click()
        dropdown = self.app.driver.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, contact.bday1).click()
        self.app.driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(16)").click()
        dropdown = self.app.driver.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, contact.bmonth1).click()
        self.app.driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(12)").click()
        self.app.driver.find_element(By.NAME, "byear").send_keys(contact.byear1)
        self.app.driver.find_element(By.NAME, "aday").click()
        dropdown = self.app.driver.find_element(By.NAME, "aday")
        dropdown.find_element(By.XPATH, contact.aday2).click()
        self.app.driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(15)").click()
        self.app.driver.find_element(By.NAME, "amonth").click()
        dropdown = self.app.driver.find_element(By.NAME, "amonth")
        dropdown.find_element(By.XPATH, contact.amonth2).click()
        self.app.driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(13)").click()
        self.app.driver.find_element(By.NAME, "ayear").send_keys(contact.ayear2)
        self.app.driver.find_element(By.NAME, "address2").click()
        self.app.driver.find_element(By.NAME, "address2").send_keys(contact.address2)
        self.app.driver.find_element(By.NAME, "phone2").click()
        self.app.driver.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        self.app.driver.find_element(By.NAME, "notes").click()
        self.app.driver.find_element(By.NAME, "notes").send_keys(contact.notes)
        self.app.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()


