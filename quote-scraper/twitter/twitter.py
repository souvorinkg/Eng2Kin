from bs4 import BeautifulSoup
from selenium import webdriver
import time




l=list()
o={}

target_url = "https://twitter.com/scrapingdog"


driver=webdriver.Chrome()

driver.get(target_url)
time.sleep(2)



resp = driver.page_source
driver.close()

soup=BeautifulSoup(resp,'html.parser')

try:
    o["profile_name"]=soup.find("div",{"class":"r-1vr29t4"}).text
except:
    o["profile_name"]=None

try:
    o["profile_handle"]=soup.find("div",{"class":"r-1wvb978"}).text
except:
    o["profile_handle"]=None

try:
    o["profile_bio"]=soup.find("div",{"data-testid":"UserDescription"}).text
except:
    o["profile_bio"]=None

profile_header = soup.find("div",{"data-testid":"UserProfileHeader_Items"})

try:
    o["profile_category"]=profile_header.find("span",{"data-testid":"UserProfessionalCategory"}).text
except:
    o["profile_category"]=None

try:
    o["profile_website"]=profile_header.find('a').get('href')
except:
    o["profile_website"]=None

try:
    o["profile_joining_date"]=profile_header.find("span",{"data-testid":"UserJoinDate"}).text
except:
    o["profile_joining_date"]=None

try:
    o["profile_following"]=soup.find_all("a",{"class":"r-rjixqe"})[0].text
except:
    o["profile_following"]=None

try:
    o["profile_followers"]=soup.find_all("a",{"class":"r-rjixqe"})[1].text
except:
    o["profile_followers"]=None


l.append(o)

print(l)