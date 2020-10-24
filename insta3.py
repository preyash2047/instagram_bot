from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

email = "glitterdots2020@gmail.com"
password = "@Googlehome1"
browserProfile = webdriver.ChromeOptions()
browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
browser = webdriver.Chrome('D:\chromedriver.exe', chrome_options=browserProfile)

browser.get('https://www.instagram.com/accounts/login/')
time.sleep(5) #???
emailInput = browser.find_element_by_name('username')
passwordInput = browser.find_element_by_name('password')
emailInput.send_keys(email)
passwordInput.send_keys(password)
passwordInput.send_keys(Keys.ENTER)

misc_btn_1 = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
misc_btn_1.click()
time.sleep(5)

misc_btn_2 = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
misc_btn_2.click()
time.sleep(5)


#like function
like_list = []
for x in range(1,100):
    like_list.append(random.randint(1,100))
like_list.sort()
like_list = list(set(like_list)) 

browser.get('https://www.instagram.com')
time.sleep(2)

for i in range(1,100):
    #like_btn = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[2]/div/article[4]/div[3]/section[1]/span[1]/button')
    like_btn = browser.find_element_by_tag_name('svg').find_element('aria-label="Like"')
    if i in like_list:
        print(i)
        like_btn.click()
        time.sleep(random.randint(1,10))