from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from re import sub
from decimal import Decimal
import threading

#brouser settings
browserProfile = webdriver.ChromeOptions()
browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
browser = webdriver.Chrome('D:\chromedriver.exe', chrome_options=browserProfile)

def login(enail,password):    
    browser.get('https://www.instagram.com/accounts/login/')
    time.sleep(5) #???
    emailInput = browser.find_element_by_name('username')
    passwordInput = browser.find_element_by_name('password')
    emailInput.send_keys(email)
    passwordInput.send_keys(password)
    passwordInput.send_keys(Keys.ENTER)

def misc_btn():
    #if prompt
    misc_btn_1 = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    misc_btn_1.click()
    time.sleep(2)
    
    misc_btn_2 = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    misc_btn_2.click()  
    time.sleep(2)

#for followers
#opening target's followers page
def follow_friends_followers(username,n):
    browser.get('https://www.instagram.com/' + username)
    time.sleep(3)
    followers_btn = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    followers_btn.click()
    #time to scrole followeres as much as possible
    time.sleep(60)    
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

#like function
#opening home page
def post_like(n):
    browser.get('https://www.instagram.com/')
    time.sleep(random.randint(10,50))
    #scrole till so much post
    like_btn = browser.find_elements_by_css_selector('button.wpO6b')
    for i in range(2,n,5):
        print(f"i: {i}")
        like_btn[i].click()
        time.sleep(random.randint(1,10))
        
#like phots in profile page
OtherUserId = "yash_dhakad4020"
browser.get("https://www.instagram.com/"+OtherUserId)
posts = browser.find_element_by_xpath("/html/body/div/section/main/div/header/section/ul/li/span/span").text
posts = Decimal(sub(r'[^\d.]', '', posts))
print(posts)
pic = browser.find_element_by_class_name("_9AhH0")    
pic.click()
time.sleep(2)




like = browser.find_elements_by_class_name('wpO6b ')
like[0].click()
nextPic = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
nextPic.click()
print("success")
sleep(2)
for i in range(int(posts-1)):
    like = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
    sleep(2)
    like.click()
    sleep(2)
    nextPic = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
    nextPic.click() 
    sleep(2)
    
    
#parameters to be edited
email = "glitterdots2020@gmail.com"
password = "Googlehome1"
targetUsername = ['rakhis_insta', '25', 'jaypore', '333k',"online_rakhistore",110,'rakhistoreindia',90,'rakhi_creation_20',330]
#colling methods
login(email,password)
misc_btn()

follow_friends_followers("ahmedabad_model_top_10_shootus",700)
follow_friends_followers("ahmedabad_girls_shotout",800)
follow_friends_followers("nisha.patel.85",20)
follow_friends_followers("_heena_099",20)


#scrole page
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")


followButton = browser.find_elements_by_css_selector('button.sqdOP')
for i in range(1,1393):
    print(i)
    previous_follow_btn = followButton[i]
    if (followButton[i].text == 'Follow'):
        followButton[i].click()
        time.sleep(random.randint(1,10))
        if(previous_follow_btn.text == "Follow"):
            print("previous_follow_btn Trigered")
            time.sleep(600)            