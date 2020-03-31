from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class InstaBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Chrome()

	def login(self):
		bot = self.bot
		bot.get("https://www.instagram.com/")
		time.sleep(2)

		email = bot.find_element_by_name('username')
		email.send_keys(self.username)
		email.clear()

		password = bot.find_element_by_name('password')
		password.send_keys(self.password)
		password.clear()
		password.send_keys(Keys.RETURN)
		time.sleep(3)

		notNow = bot.find_element_by_class_name('HoLwm')
		notNow.click()

		for i in range(10):
			bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
			time.sleep(2)



result = InstaBot("username", "password")
result.login()
