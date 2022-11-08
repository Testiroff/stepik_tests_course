from selenium import webdriver
import time
import math
import pytest


browser = webdriver.Chrome()
browser.get("https://stepik.org/lesson/236895/step/1")

browser.implicitly_wait(5)
answer = str(math.log(int(time.time())))
browser.find_element_by_tag_name('textarea').send_keys(answer)
browser.find_element_by_css_selector('button.submit-submission').click()


