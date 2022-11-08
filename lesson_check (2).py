from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_elements_by_xpath("//input")[0]
input1.send_keys("Ivan")
input2 = browser.find_elements_by_xpath("//input")[1]
input2.send_keys("Petrov")
input3 = browser.find_elements_by_xpath("//input")[2]
input3.send_keys("Smolensk")
input4 = browser.find_elements_by_xpath("//input")[3]
input4.send_keys("Russia")
button = browser.find_element_by_xpath("//form/div[5]/button[@type='button'][1]").click()

browser.quit()
