from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration1.html")
browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input").send_keys("Ivan")
browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input[@class='form-control second' and @required]").send_keys("Ivanov")
browser.find_element_by_xpath("//form/div[1]/div[3]/input[@class='form-control third' and @required]").send_keys("Ivan@mail.ru")
button = browser.find_element_by_xpath("//form//button[@type='submit']").click()
time.sleep(5)
browser.quit()

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration2.html")
browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input").send_keys("Ivan")
browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input[@class='form-control second' and @required]").send_keys("Ivanov")
browser.find_element_by_xpath("//form/div[1]/div[3]/input[@class='form-control third' and @required]").send_keys("Ivan@mail.ru")
button = browser.find_element_by_xpath("//form//button[@type='submit']").click()

browser.quit()
