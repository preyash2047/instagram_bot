from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from re import sub
from decimal import Decimal
import threading

class instagramBot():
    def __init__(self,email,password):
        #parameters
        self.normal_wait_time = 3
        self.miss_btn1_xpath = "/html/body/div[1]/section/main/div/div/div/div/button"
        self.miss_btn2_xpath = "/html/body/div[4]/div/div/div/div[3]/button[2]"
        #in user profile
        self.followers_count_xpath = "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span"
        #inside list of followers
        self.followers_btn_xpath =  "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a"
        self.scroll_followers_list_xpath = '//div[@class="isgrP"]//a'
        self.usersname_inside_followers_class = "FPmhX"
        
        #ignore last followers or count
        self.ignore_count = 50
        
        #follow from username:
        self.privateOrNot_xpath = '//*[@id="react-root"]/section/main/div/div/article/div/div/h2'
        self.follow_btn_insideprofile_xpath = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button'
        self.follow_btn_inside_followers_list_class = "Pkbci"
        
        
        
        #brouser settings
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('C:\chromedriver.exe', chrome_options=self.browserProfile)
            
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(self.normal_wait_time)
        self.emailInput = self.browser.find_element_by_name('username')
        self.passwordInput = self.browser.find_element_by_name('password')
        self.emailInput.send_keys(email)
        self.passwordInput.send_keys(password)
        self.passwordInput.send_keys(Keys.ENTER)
        
        time.sleep(self.normal_wait_time)
        #click on miscelinous buttons
        self.btn1 = self.browser.find_element_by_xpath(self.miss_btn1_xpath)
        self.btn1.click()
        time.sleep(self.normal_wait_time)
        self.btn2 = self.browser.find_element_by_xpath(self.miss_btn2_xpath)
        self.btn2.click()
        time.sleep(self.normal_wait_time)
            
        
    #will copy_followers from username and return list
    def copy_followers(self,username):
        self.browser.get('https://www.instagram.com/'+str(username))
        time.sleep(self.normal_wait_time)
        self.followersCount = self.browser.find_element_by_xpath(self.followers_count_xpath)
        self.followersBtn = self.browser.find_element_by_xpath(self.followers_btn_xpath)
        self.followersBtn.click()
        self.followersCount = int(self.followersCount.get_attribute('title').replace(",",""))
        if self.followersCount >= self.ignore_count:
            for i in range(int(self.followersCount/11)):
                time.sleep(self.normal_wait_time)
                self.element_inside_popup = self.browser.find_element_by_xpath(self.scroll_followers_list_xpath)
                self.element_inside_popup.send_keys(Keys.END)
            
            self.followButton = self.browser.find_elements_by_class_name(self.usersname_inside_followers_class)    
            self.listofusers = [i.text for i in self.followButton]
            return self.listofusers
        else:
            return None
            
    def follow_from_list(self,followers_list):
        for i in followers_list:
            time.sleep(self.normal_wait_time)
            self.browser.get('https://www.instagram.com/'+str(i))
            time.sleep(self.normal_wait_time)
            try:
                self.privateOrNot = self.browser.find_element_by_xpath(self.privateOrNot_xpath)
                if self.privateOrNot.text.split()[-1] == "Private":
                    self.followbtn = self.browser.find_element_by_xpath(self.follow_btn_insideprofile_xpath)
                    self.followbtn.click()
            except:
                pass
                    
    def follow_from_username(self,username,count,sleep_count):
        self.browser.get('https://www.instagram.com/'+str(username))
        time.sleep(self.normal_wait_time)
        self.followersCount = self.browser.find_element_by_xpath(self.followers_count_xpath)
        self.followersBtn = self.browser.find_element_by_xpath(self.followers_btn_xpath)
        self.followersBtn.click()
        self.followersCount = int(self.followersCount.get_attribute('title').replace(",",""))
        if self.followersCount >= min(self.ignore_count,count):
            for i in range(int(count/11)):
                time.sleep(self.normal_wait_time)
                self.element_inside_popup = self.browser.find_element_by_xpath(self.scroll_followers_list_xpath)
                self.element_inside_popup.send_keys(Keys.END)
            
            self.followButtons = self.browser.find_elements_by_class_name(self.follow_btn_inside_followers_list_class)    
            self.followButtons[0].click()
            time.sleep(self.normal_wait_time)
            for i in range(1,len(self.followButtons)):
                if self.followButtons[i-1].text == "Follow":
                    time.sleep(200)
                else:
                    self.followButtons[i].click()
                    time.sleep(random.randint(1, 10))
                    



#obj creation will lead to the home page        
obj = instagramBot(email = "glitterdots2020@gmail.com", password = "Googlehome1")

followers = obj.copy_followers(username="theorganic__tales")
temp_list = followers[:10]    
obj.follow_from_list(followers_list = temp_list[5:])

obj.follow_from_username(username = "flirt.karo", count = 23,sleep_count = 600)


    