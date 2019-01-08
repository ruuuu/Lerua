# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:12:44 2018

@author: usse
"""




import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains # lля сколддинга к нужному элементу импортируем класс ActionChains


import time



class filtr_ideas(unittest.TestCase):

    def authorization(self, driver):  # авторизация

        driver.get('https://admin:LY1R1VMXJ1@dev.leroyfactory.ru')  # чтобы обойти базовую аунтентификацию
        # driver.get("https://dev.leroyfactory.ru/main")

        #кнопка Войти:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH,
                                                 "//a[@class='link link-block']")))[6].click()

        time.sleep(2)
        # атворизуемся
        login = driver.find_element_by_xpath("//input[@formcontrolname='login']")
        login.send_keys("admin@mail.ru")

        time.sleep(2)
        password_d = driver.find_element_by_xpath("//input[@formcontrolname='password']")
        password_d.send_keys("password")

        time.sleep(2)
        but_send = driver.find_element_by_xpath("//button[@class ='btn-green btn signin-submit-button']")  # отправть
        but_send.click()


    def poisk(self, driver):# поиск идеи по названию

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn search-btn']"))).click() #  поле поиска

        time.sleep(2)
        result = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Найти идею по названию']")))

        result.send_keys("video")
        result.send_keys(Keys.ENTER) # нажатие клавиши ентер
        time.sleep(3)

        #надимае на кретсик красный:
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn ideas-search-query-remove']"))).click()


    def dump_filter(self, driver):

        # сброс фильтров всех:
        #
        # Раздел "Любая стоимость":
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[3].click()

        time.sleep(2)
        # "Выбрать все" выбираем
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-default']")))[3].click()

        time.sleep(2)
        # Раздел "Любое время":
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[2].click()

        time.sleep(2)
        # "Выбрать все" выбираем
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-default']")))[2].click()

        # Раздел "Любая сложность":
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[1].click()

        time.sleep(2)
        # "Выбрать все" выбираем
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-default']")))[1].click()

        # Раздел "Любые материалы":
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[0].click()

        # "Выбрать все" выбираем
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-default']")))[0].click()

        time.sleep(4)



    def filter_by_favorite_my_last_popularity(self, driver): # фильтр по Последние, Популярные Избраннеы Мои

        for i in range(0, 4):
            time.sleep(1)
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//label[@class='sorting-item']")))[i].click()
            k = 0
            while k < 200:  # чтобы скроллиить к  концу станицы
                scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
                k += 1
            #time.sleep(1)
            k = 0
            while k < 230:  # чтобы скроллиить к  концу станицы
                scroll = driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_UP)  # скроллит станицу наверх
                k += 1
            #time.sleep(1)







    def setUp(self):

        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
            "browserName": "chrome",
        })
         #self.driver.maximize_window()
        # self.driver.implicitly_wait(10)



    def test_filter_idea_method(self):

        driver = self.driver

        self.authorization(driver)  # вызов метода  авторизации,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось


        # кликаем на раздел Идеи:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//a[@href='/idei']"))).click()

        time.sleep(2)


        # Раздел "Любые материалы":
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[0].click()

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-params-item']")))[1].click() # металл выбрали
        time.sleep(1)
        k = 0
        while k < 200:  # чтобы скроллиить к  концу станицы
            scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
            k += 1
        time.sleep(1)
        k = 0
        while k < 200:  # чтобы скроллиить к  концу станицы
            scroll = driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_UP)  # скроллит станицу наверх
            k += 1
        time.sleep(1)


        # Раздел "Любая сложность":

        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[1].click()

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-params-item']")))[5].click()  # средне  выбрали
        time.sleep(1)
        k = 0
        while k < 200:  # чтобы скроллиить к  концу станицы
            scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
            k += 1
        time.sleep(1)
        k = 0
        while k < 200:  # чтобы скроллиить к  концу станицы
            scroll = driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_UP)  # скроллит станицу наверх
            k += 1
        time.sleep(1)

        # Раздел "Любое время":

        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[2].click()

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-params-item']")))[9].click()  # от 3 ч до 1 дня  выбрали
        time.sleep(1)
        k = 0
        while k < 200:  # чтобы скроллиить к  концу станицы
            scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
            k += 1
        time.sleep(1)
        k = 0
        while k < 200:  # чтобы скроллиить к  концу станицы
            scroll = driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_UP)  # скроллит станицу наверх
            k += 1
        time.sleep(1)

        # Раздел "Любая стоимость":

        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[3].click()

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-params-item']")))[11].click()  # до 1000 р  выбрали
        time.sleep(1)
        k = 0
        while k < 200:  # чтобы скроллиить к  концу станицы
            scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
            k += 1
        time.sleep(1)
        k = 0
        while k < 200:  # чтобы скроллиить к  концу станицы
            scroll = driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_UP)  # скроллит станицу наверх
            k += 1
        time.sleep(1)

        self.dump_filter(driver)  # сброс фильтров
        time.sleep(1)

        self.filter_by_favorite_my_last_popularity(driver)  # вызываем меод
        time.sleep(1)

        self.poisk(driver)  # вызов метода выше



    def tear_down(self):
        self.driver.quit()
        self.driver.close()
        # pass


if __name__ == "__main__":
    unittest.main()






