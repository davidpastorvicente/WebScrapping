from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.149 Safari/537.36")

driver = webdriver.Chrome("chromedriver.exe", options=opts)

driver.get("https://showrss.info/login")

driver.find_element_by_id("username").send_keys("david15pastor")
driver.find_element_by_id("password").send_keys(open('password.txt').readline())
driver.find_element_by_class_name("btn").click()

shows = driver.find_elements_by_xpath("//a[@class='sh']")

for show in shows:
    print(show.get_attribute("title"))
