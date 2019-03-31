# -*- coding: utf-8 -*-
"""
Created on Sat May 12 12:16:53 2018

@author: usse
"""



import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome() 
driver.get("https://leroy-fabrica.herokuapp.com/ideas?creation=idea")

# загрузка файла
# элемент ниже <input _ngcontent-c83="" ng2fileselect="" type="file">
element1 = driver.find_element(by=By.XPATH, value="/html/body/app-root/app-idea-creation/div/form/div[2]/div/app-single-media-picker/label/input") # берем элемент input type='file'
element1.send_keys("C:\\Users\\usse\\Desktop\\для теста_Леруа\\dog.jpg")
#element1.send_keys(Keys.ENTER)

element2= driver.find_element(by=By.XPATH, value="/html/body/app-root/app-idea-creation/div/form/div[1]/div[1]/section[7]/div[2]/app-file-picker/div/div/label/input") 
element2.send_keys("C:\\Users\\usse\\Desktop\\для теста_Леруа\\2G-HOLI.jpeg") 