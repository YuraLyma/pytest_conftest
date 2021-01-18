import time

from selenium.common.exceptions import NoSuchElementException


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_baskett(browser):
	browser.get(link)
	time.sleep(30)
	try:
		btn = browser.find_element_by_css_selector(".btn-add-to-basket")
	except NoSuchElementException:
		btn = False

	assert btn, 'There are no "Add to basket" buttons'
