from django.test import TestCase
from selenium import webdriver
from .forms import HashForm
import hashlib
from .models import Hash

# class FunctionalTestCase(TestCase):
# 	def setUp(self):
# 		self.browser = webdriver.Firefox()

# 	def test_there_is_homepage(self):
# 		self.browser.get('http://127.0.0.1:8000/')
# 		self.assertIn('Enter hash here:',self.browser.page_source)

# 	def test_hash_of_hello(self):
# 		self.browser.get('http://127.0.0.1:8000/')
# 		text = self.browser.find_element_by_id('id_text')
# 		text.send_keys('hello')
# 		self.browser.find_element_by_name('submit').click()
# 		self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',self.browser.page_source)
		
# 	def tearDown(self):
# 		self.browser.quit()

class UnitTestCase(TestCase):

	def test_home_homepage_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'hashing/home.html')

	def test_hash_form(self):
		form = HashForm(data={'text':'hello'})
		self.assertTrue(form.is_valid())

	def saveHash(self):
		Hash1 = Hash()
		Hash1.text = 'hello'
		Hash1.Hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
		Hash1.save()
		return Hash1

	def test_hash_func_works(self):
		text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
		self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',text_hash)

	def test_hash_object(self):
		Hash1 = self.saveHash()
		pulled_hash = Hash.objects.get(Hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
		self.assertEqual(Hash1.text,pulled_hash.text)

	def test_viewing_hash(self):
		Hash1 = self.saveHash()
		response = self.client.get('/hash/2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
		self.assertContains(response,'hello')


