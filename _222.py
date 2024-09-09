from selenium import webdriver   
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://www.ebay.com/")
driver.maximize_window()
time.sleep(5)

electronics_xpath = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/ul/li[3]/a")
electronics_xpath.click()
time.sleep(2)

samsung_xpath = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[3]/section[2]/div[2]/span[5]/a")
samsung_xpath.click()
time.sleep(2)
phones_xpath = driver.find_element(By.XPATH,"/html/body/div[3]/nav/div[1]/div/div/div/section/ul/li[3]/a")
phones_xpath.click()
time.sleep(2)
for i in range(1,60):
    xpath = "/html/body/div[3]/div[3]/div[3]/section[3]/ul/li[" +str(i)+ "]/div[1]/div[1]/div/a/div/div/img"
    image = driver.find_element(By.XPATH,xpath)
    image.screenshot("img("+str(i)+").png")
    print("done")
    
    

   




# data = []
# 
# 
# for i in range(1,20):
#     xpath = "/html/body/div/div/div/div/section/div[2]/ol/li[" +str(i)+ "]"
#     list_ = driver.find_element(By.XPATH,xpath)
#     text = list_.text
#     data.append(text)
#     df = pd.DataFrame(data)
#     print(df)
# 
# next_link = driver.find_element(By.XPATH,"/html/body/div/div/div/div/section/div[2]/div/ul/li[2]/a")
# next_link.click()
# time.sleep(2)
# # 
# data_2 = []
# 
# 
# 
# for o in range(1,20):
#     xpath_2 = "/html/body/div/div/div/div/section/div[2]/ol/li[" +str(o)+ "]"
#     list_2 = driver.find_element(By.XPATH,xpath_2)
#     text_2 = list_2.text
#     data_2.append(text_2)
#     df_2 = pd.DataFrame(data_2)
#     print(df_2)
    
#     
# 
# life_link = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/span[3]/a")
# life_link.click()
# time.sleep(2)
# 
# data_3 = []
# 
# head_3 = driver.find_element(By.XPATH,"/html/body/div/h3")
# head_text_3 = head_3.text
# print(head_text_3)
# 
# 
# for u in range(1,10):
#     xpath_3 = "/html/body/div/div[2]/div[1]/div["+ str(u) +"]"
#     list_3 = driver.find_element(By.XPATH,xpath_3)
#     text_3 = list_3.text
#     data_3.append(text_3)
#     df_3 = pd.DataFrame(data_3)
#     print(df_3)
#     
# humor_link = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/span[4]/a")
# humor_link.click()
# time.sleep(2)
# 
# data_4 = []
# 
# head_4 = driver.find_element(By.XPATH,"/html/body/div/h3")
# head_text_4 = head_4.text
# print(head_text_4)
# 
# 
# for l in range(1,10):
#     xpath_4 = "/html/body/div/div[2]/div[1]/div["+ str(l) +"]"
#     list_4 = driver.find_element(By.XPATH,xpath_4)
#     text_4 = list_4.text
#     data_4.append(text_4)
#     df_4 = pd.DataFrame(data_4)
#     print(df_4)
#     
# books_link = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/span[5]/a")
# books_link.click()
# time.sleep(2)
# 
# data_5 = []
# 
# head_5 = driver.find_element(By.XPATH,"/html/body/div/h3")
# head_text_5 = head_5.text
# print(head_text_5)
# 
# 
# for p in range(1,10):
#     xpath_5 = "/html/body/div/div[2]/div[1]/div["+ str(p) +"]"
#     list_5 = driver.find_element(By.XPATH,xpath_5)
#     text_5 = list_5.text
#     data_5.append(text_5)
#     df_5 = pd.DataFrame(data_5)
#     print(df_5)
    



