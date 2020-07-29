import random
from time import sleep
from selenium import webdriver

print('Introducir búsqueda: ')
txt = input().replace(' ', '%20')

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://es.wallapop.com/search?keywords=' + txt)
sleep(3)
driver.find_element_by_id('didomi-notice-agree-button').click()

driver.find_element_by_xpath("//div[@id='more-products-btn']//button").click()
sleep(3)
cars = driver.find_elements_by_xpath("//div[@class = 'card js-masonry-item card-product product tracked']")

i = 1
for car in cars:
    print('Resultado', i)
    print('\tNombre:', car.find_element_by_class_name('product-info-title').text.strip())
    print('\tPrecio:', car.find_element_by_class_name('product-info-price').text.strip())
    print()
    i += 1