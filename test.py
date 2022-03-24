from optparse import Values
from select import select
from time import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
site = "https://www.thesparksfoundationsingapore.org/"
driver.get(site)
 
#Element 1 check the title is the same or Not
if driver.title == "The Sparks Foundation | Home":
  print("test 1 successful => title matched ")
else:
  print("test 1 failed => title not matched ")
  
words = ["About Us","Policies and Code","Programs","LINKS","Join Us","Contact Us"]
for index,word in enumerate(words):
   link_2 = driver.find_element_by_link_text(word)
   if link_2.is_enabled():
      print("Test ",index," Successful => ",word," Exists")
   else:
      print("Test ",index," failed")
      
      
open_drop_menu1 = driver.find_element_by_link_text("About Us").click()
vocabs = ["Vision, Mission and Values","Guiding Principles","Advisors and Patrons","Executive Team","Corporate Partners","Expert Mentors","News"]
for index,vocab in enumerate(vocabs):
 link3 = driver.find_element_by_link_text(vocab)
 if link3.is_enabled():
  print("Test",index,"Successful => ",vocab)
 else:
  print("Test",index,"failed => ",vocab)


open_drop_menu2 = driver.find_element_by_link_text("Policies and Code").click()
highlights = ["Policies","Code of Ethics and Conduct","Personal Data Policy","Whistle Blowing Policy","Service Quality Values"]
for index,highlight in enumerate(highlights):
 link4 = driver.find_element_by_link_text(highlight)
 if link4.is_enabled():
      print("Test",index,"Successful => ",highlight)
 else:
  print("Test",index,"failed => ",highlight)


open_drop_menu3 = driver.find_element_by_link_text("Programs").click()
values = ["Student Scholarship Program","Student Mentorship Program","Student SOS Program","Workshops","Corporate Programs"]
for index,value in enumerate(values):
 link5 = driver.find_element_by_link_text(value)
 if link5.is_enabled():
      print("Test",index,"Successful => ",value)
 else:
  print("Test",index,"failed => ",value)


open_drop_menu4 = driver.find_element_by_link_text("LINKS").click()
nums = ["Software & App","Salient Features","AI in Education"]
for index,num in enumerate(nums):
 link6 = driver.find_element_by_link_text(num)
 if link6.is_enabled():
      print("Test",index,"Successful => ",num)
 else:
  print("Test",index,"failed => ",num)


open_drop_menu4 = driver.find_element_by_link_text("Join Us").click()
ds= ["Why Join Us","Expert Mentor","Events Volunteer","Management Volunteer","Internship Positions","Brand Ambassador","KNOW MORE","LEARN MORE","VISIT NOW","EXPLORE","GRIP (Internship)"]
for index,d in enumerate(ds):      
 link7 = driver.find_element_by_link_text(d)
 if link7.is_enabled():
      print("Test",index,"Successful => ",d)
 else:
  print("Test",index,"failed => ",d)
 
 # Check The PAGES are working or Not
element1 = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/a")
element1.click()
if element1.is_enabled():
      print("Test 39 Successful => Know More Page loaded")
else:
      print("Test 39 failed")
      
element2 = driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[1]/ul/li[1]/a")
element2.click()
if element2.is_enabled():
      print("Test 40 Successful => Xaltius Page loaded")
else:
      print("Test 40 failed")
      
element3 = driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[3]/ul/li/a")
element3.click()
if element3.is_enabled():
      print("Test 41 Successful => ernships at Internshala Page loaded")
else:
      print("Test 41 failed")
      
element4 = driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[1]/ul/li[2]/a")
element4.click()
if element4.is_enabled():
      print("Test 42 Successful => AINE AI Page loaded")
else:
      print("Test 42 failed")

element5 = driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[2]/ul/li[3]/a")
element5.click()
if element5.is_enabled():
      print("Test 43 Successful => Jobs at Tech in Asia Portal Page loaded")
else:
      print("Test 43 failed")

time.sleep(10)
driver.quit()
 