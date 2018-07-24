from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

chromepath = r"chromepath"
# set your chrome driver path here ^


#Fill in your info here


name = "Full name as on ID"

phone = "phone number"

prefix = "gmail prefix"

size = "size. only 8, 9, 10, 11 are supported"










print("ShoeGallery Raffle script by Tracy#1111")
driver = webdriver.Chrome(chromepath)



while True:
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfeDtXzO3WYUlffDwVdUNRVFpJyT_i96U3gbQY8cyVTKNk2KQ/viewform')

    email = (prefix + "+" + str(random.randint(0, 9999)) + "@gmail.com")

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/input').send_keys(name)

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div[2]/div/div[1]/div/div[1]/input').send_keys(phone)

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div[2]/div/div[1]/div/div[1]/input').send_keys(email)

    if size == "11":
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div[2]/div/content/div/label[8]/div/div[1]/div[3]/div').click()

    if size == "10":
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div[2]/div/content/div/label[7]/div/div[1]/div[3]/div').click()

    if size == "9":
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div[2]/div/content/div/label[6]/div/div[1]/div[3]/div').click()

    if size == "8":
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div[2]/div/content/div/label[5]/div/div[1]/div[3]/div/div').click()

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div/content/span').click()
    print(' ')
    print("Successfully entered raffle with email - " + email)

    time.sleep(5)