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

        driver.get('https://admin:LY1R1VMXJ1@leroyfactory.ru')  # чтобы обойти базовую аунтентификацию
        # driver.get("https://dev.leroyfactory.ru/main")

        #кнопка Войти:
        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH,
                                                 "//a[@class='link link-block']")))[6].click()

        time.sleep(2)
        # атворизуемся
        login = driver.find_element_by_xpath("//input[@formcontrolname='login']")
        login.send_keys("superadmin@mail.ru")

        time.sleep(2)
        password_d = driver.find_element_by_xpath("//input[@formcontrolname='password']")
        password_d.send_keys("J5mmwxN5NeqpX3cd")

        time.sleep(2)
        but_send = driver.find_element_by_xpath("//button[@class ='btn-green btn signin-submit-button']")  # отправть
        but_send.click()


    def poisk(self, driver):# поиск идеи по названию

        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn search-btn']"))).click() #  поле поиска

        time.sleep(2)
        result = WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Найти идею по названию']")))

        time.sleep(2)
        result.send_keys("test_idea")
        result.send_keys(Keys.ENTER) # нажатие клавиши ентер
        time.sleep(3)

        #надимае на кретсик красный:
        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn ideas-search-query-remove']"))).click()


    def dump_filter(self, driver):

        # сброс фильтров всех:
        #
        # Раздел "Любая стоимость":
        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[3].click()

        time.sleep(2)
        # "Выбрать все" выбираем
        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-default']")))[3].click()

        time.sleep(2)
        # Раздел "Любое время":
        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[2].click()

        time.sleep(2)
        # "Выбрать все" выбираем
        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-default']")))[2].click()

        # Раздел "Любая сложность":
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[1].click()

        time.sleep(2)
        # "Выбрать все" выбираем
        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-default']")))[1].click()

        # Раздел "Любые материалы":
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[0].click()

        # "Выбрать все" выбираем
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-default']")))[0].click()

        time.sleep(4)



    def filter_by_favorite_my_last_popularity(self, driver): # фильтр по Последние, Популярные Избраннеы Мои

        for i in range(0, 4):#

            time.sleep(1)
            WebDriverWait(driver, 20).until(
                ec.presence_of_all_elements_located((By.XPATH, "//label[@class='sorting-item']")))[i].click()
            time.sleep(1)
            # k = 0
            # while k < 200:  # чтобы скроллиить к  концу станицы
            #     scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
            #     k += 1
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN) # переходим вниз станицы
            time.sleep(3)
            # k = 0
            # while k < 230:  # чтобы скроллиить к началу станицы
            #      scroll = driver.find_element_by_tag_name('body').send_keys(Keys.UP)  # скроллит станицу наверх переходим вверх станицы
            #      k += 1
            # time.sleep(1)


            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)#скроллит станицу наверх переходим вверх станицы






    def setUp(self):

        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
            "browserName": "chrome",
        })
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        # # увеличит размер экрана
        # zoomAction = ActionChains(self.driver)
        # body = self.driver.find_element_by_tag_name('body')
        # for i in range(2):
        #     zoomAction.send_keys_to_element(body, Keys.CONTROL, "+").perform()
        #


         #self.driver.maximize_window()
        # self.driver.implicitly_wait(10)



    def test_filter_idea_method(self):

        driver = self.driver

        self.authorization(driver)  # вызов метода  авторизации,котрый выше
        time.sleep(8)  # чтобы сразу окно не закрывалось


        # кликаем на раздел Идеи:
        ideas = WebDriverWait(driver, 20).until(ec.presence_of_element_located(
                (By.XPATH, "//a[@href='/idei']")))

        time.sleep(2)
        try:
            ideas.click()
        except:
            time.sleep(6)
            ideas.click()




        # Раздел "Любые материалы":
        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[0].click()

        time.sleep(2)
        WebDriverWait(driver, 20).until(
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

        time.sleep(4)
        # Раздел "Любая сложность":

        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[1].click()

        time.sleep(2)
        WebDriverWait(driver, 20).until(
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

        time.sleep(4)
        # Раздел "Любое время":

        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[2].click()

        time.sleep(2)
        WebDriverWait(driver, 20).until(
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

        time.sleep(4)
        # Раздел "Любая стоимость":

        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-lg-none']")))[3].click()

        time.sleep(2)
        WebDriverWait(driver, 20).until(
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
        time.sleep(4)

        self.poisk(driver)  # вызов метода выше



    def tear_down(self):
        self.driver.quit()
        #self.driver.close()
        # pass


if __name__ == "__main__":
    unittest.main()






