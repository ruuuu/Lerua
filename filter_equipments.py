# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:46:56 2018

@author: usse
"""

import time
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# фильрация оборудований
class Filter_equipments(unittest.TestCase):


    def authorization(self, driver):  # авторизация

        driver.get('https://admin:LY1R1VMXJ1@dev.leroyfactory.ru')  # чтобы обойти базовую аунтентификацию
        # driver.get("https://dev.leroyfactory.ru/main")

        time.sleep(2)
        #кнопка Войти:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH,
                                                 "//a[@class='link link-block']")))[6].click()

        time.sleep(2)
        # атворизуемся
        login = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='login']")))
        login.send_keys("admin@mail.ru")

        time.sleep(2)
        password_d = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']")))
        password_d.send_keys("password")

        time.sleep(2)
        but_send = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class ='btn-green btn signin-submit-button']")))  # отправть
        but_send.click()


    def poisk(self, driver): # поис по названию

        time.sleep(2)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class ='btn search-btn']"))).click() # поле поиска

        time.sleep(1)
        result = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@type ='search']")))
        #time.sleep(2)

        result.send_keys("единое мое")
        time.sleep(2)
        result.send_keys(Keys.ENTER)# нажатие клавиши ентер



        time.sleep(3)

        # надимае на кретсик красный:
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn equipment-search-query-remove']"))).click()


    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера

        #self.driver.fullscreen_window()  # откроет браузер на весь экзан

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, чтобы подгруздимь элементы



    def test_filters_equipment(self):

        driver = self.driver
        self.authorization(driver)  # вызываем метод, котрый выше
        time.sleep(3)
        #
        try:#
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/oborudovanie']"))).click() #код будет ждать 10 секунд до того, как отдаст исключение TimeoutException или если найдет элемент за эти 10 секунд, то вернет его.
        except TimeoutError:
            pass  # ничего не будет делать


        time.sleep(2)# чтобы посомртеть что происходит


        try:
          for i in range(0, 3):  # цикл по фильтрам

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//label[@class='sorting-item']")))[i].click()

            time.sleep(1)
            if i == 0:  # если фильтр по протсрнатсву:
                time.sleep(1)
                for j in range(0, 10):
                    if (j > 5 or j == 5):
                        break # выход из вн цикла
                    elem_filtr = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,
                                                                                         "//label[@class='filter-item-wrapper']")))[j*2+1].click()
                    time.sleep(1)
                    k = 0
                    while k < 200:  # чтобы скроллиить к  концу станицы
                         scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
                         k += 1
                    time.sleep(1)
                    k = 0
                    while k < 200:  # чтобы скроллиить к  концу станицы
                         scroll = driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_UP) # скроллит станицу наверх
                         k += 1
                    time.sleep(1)

            time.sleep(1)
            if i == 1:# если фильтр по матералу:
                time.sleep(1)
                for j in range(0, 7):
                    if (j > 3 or j ==3 ):
                        break
                    WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,
                                                                                         "//label[@class='filter-item-wrapper']")))[j*2+1].click()
                    time.sleep(1)

                    k = 0
                    while k < 200:  # чтобы скроллиить к  концу станицы
                        scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
                        k += 1
                    time.sleep(1)
                    k = 0
                    while k < 200:  # чтобы скроллиить к  концу станицы
                        scroll = driver.find_element_by_tag_name('body').send_keys(
                            Keys.ARROW_UP)  # скроллит станицу наверх
                        k += 1
                    time.sleep(1)

            time.sleep(1)
            if i == 2: # если фильтр по Назначение :
                time.sleep(1)
                WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,
                                                                                     "//label[@class='sorting-item']")))[i].click()

                for j in range(0, 10):
                    if (j > 5 or j==5):
                        break # выход из вн цикла
                    WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,
                                                                                         "//label[@class='filter-item-wrapper']")))[j*2+1].click()
                    time.sleep(1)

                    k = 0
                    while k < 200:  # чтобы скроллиить к  концу станицы
                        scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
                        k += 1
                    time.sleep(1)
                    k = 0
                    while k < 200:  # чтобы скроллиить к  концу станицы
                        scroll = driver.find_element_by_tag_name('body').send_keys(
                            Keys.ARROW_UP)  # скроллит станицу наверх
                        k += 1
                    time.sleep(1)


        except TimeoutError:
           pass


        #self.poisk(driver) # вызов метода выше не хочет рабоать



    def tear_down(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()










