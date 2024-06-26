import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class use_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_explicit_wait(self):
		driver = self.driver
		driver.get("http://www.google.com")
		try:
			element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"q")))
		finally:
			driver.quit()

if __name__ == '__main__':
	unittest.main()