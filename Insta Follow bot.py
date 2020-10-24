from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from re import sub
from decimal import Decimal
import threading

#input
email,password = "glitterdots2020@gmail.com", "Googlehome1"

#brouser settings
browserProfile = webdriver.ChromeOptions()
browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
browser = webdriver.Chrome('C:\chromedriver.exe', chrome_options=browserProfile)

#def login(email,password):    
browser.get('https://www.instagram.com/accounts/login/')
time.sleep(5) #???
emailInput = browser.find_element_by_name('username')
passwordInput = browser.find_element_by_name('password')
emailInput.send_keys(email)
passwordInput.send_keys(password)
passwordInput.send_keys(Keys.ENTER)
#click on miscelinous buttons
btn1 = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
btn1.click()
time.sleep(2)
btn2 = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
btn2.click()    
    
#getting list of followers
coppyFollowersFrom = ["fashionworldjewellery", "jewellery.creation20", "jewellery_house_1"]
browser.get('https://www.instagram.com/'+str(coppyFollowersFrom[0]))
time.sleep(3)
followersCount = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")
followersBtn = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
followersBtn.click()
for i in range(int(int(followersCount.text)/11)):
    time.sleep(random.randint(1, 2))
    element_inside_popup = browser.find_element_by_xpath('//div[@class="isgrP"]//a')
    element_inside_popup.send_keys(Keys.END)

#grab followers    
followButton = browser.find_elements_by_class_name('FPmhX')    
listofusers = [i.text for i in followButton]
requestSentCount = 0
#staring Following people with private account
for i in listofusers:   
    time.sleep(random.randint(0, 6))
    browser.get('https://www.instagram.com/'+str(i))
    time.sleep(3)
    try:
        privateOrNot = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div/div/h2")
        if privateOrNot.text.split()[-1] == "Private":
            followbtn = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/button")
            followbtn.click()
            requestSentCount += 1
    except:
        pass

    
#follow users from home page
#open post you want to followe who has liked the post
NoofLikes = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/div/button")
NoofLikes.click()
time.sleep(2)
for i in range(int(int(NoofLikes.text.split()[0])/11)):
    time.sleep(random.randint(1, 2))
    element_inside_popup = browser.find_element_by_xpath('//div[@class="                    Igw0E   rBNOH        eGOV_     ybXk5    _4EzTm                                                                                   XfCBB          HVWg4                 "]//a')
    element_inside_popup.send_keys(Keys.END)
    
followButton = browser.find_elements_by_css_selector('button.sqdOP')
for i in range(1,n):
    print(i)
    previous_follow_btn = followButton[i]
    if (followButton[i].text == 'Follow'):
        followButton[i].click()
        time.sleep(random.randint(1,10))
        if(previous_follow_btn.text == "Follow"):
            print("previous_follow_btn Trigered")
            time.sleep(600)     