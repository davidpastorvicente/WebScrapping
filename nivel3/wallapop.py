from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

print('Introducir búsqueda: ')
txt = input().replace(' ', '%20')

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://es.wallapop.com/search?keywords=' + txt)

WebDriverWait(driver, 5).until(
    expected_conditions.presence_of_element_located((By.XPATH, "//button[@id='didomi-notice-agree-button']"))).click()

driver.find_element_by_xpath("//div[@id='more-products-btn']//button").click()

WebDriverWait(driver, 5).until(
    expected_conditions.presence_of_all_elements_located((By.XPATH,
                                                          "//div[@class = 'card js-masonry-item card-product "
                                                          "product tracked']//span[@class='product-info-title']")))

cars = driver.find_elements_by_xpath("//div[@class = 'card js-masonry-item card-product product tracked']")

i = 1
for car in cars:
    print('Resultado', i)
    print('\tNombre:', car.find_element_by_class_name('product-info-title').text.strip())
    print('\tPrecio:', car.find_element_by_class_name('product-info-price').text.strip())
    print()
    i += 1
