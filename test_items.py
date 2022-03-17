import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket").is_displayed(), 'Button not visible'
    time.sleep(30)
	