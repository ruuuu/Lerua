# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:28:13 2018

@author: usse
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



# фильтрация  по разным категориям на старнице курсов:
class Filter_course_test(unittest.TestCase):

    def authorization(self, driver):  # авторизация

        driver.get('https://admin:LY1R1VMXJ1@dev.leroyfactory.ru')  # чтобы обойти базовую аунтентификацию
        # driver.get("https://dev.leroyfactory.ru/main")

        # кнопка Войти:
        button_voity = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//a[@class='link link-block']")))[6]
        button_voity.click()

        #  поле Логин
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='login']"))).send_keys("admin@mail.ru")

        #  поле ПАРОЛЬ
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys(
            "password")

        # кнопка Войти в форме авторизации
        voity = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn-green btn signin-submit-button']")))

        if voity.is_displayed():  # если кнпока видна , то
            voity.click()



    def setUp(self):

            self.driver = webdriver.Chrome()

            self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
            self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера

            #self.driver.maximize_window()
            #self.driver.implicitly_wait(10) # для  явных ожиданий, чтобы подгруздимь элементы
            

    def test_filter(self):

            driver = self.driver
            self.authorization(driver) # вызоав метода

            time.sleep(6)# ждем пока загрузится главная старница

            elem_link = driver.find_element_by_link_text('Обучение')
            elem_link.click()

            time.sleep(6)# ждем пока загрузится  старница всех курсов

            # # жмем на пердуыдщий месяц
            # filtrmonth_prev = WebDriverWait(driver, 10).until(
            #     ec.presence_of_element_located("//button[@class='btn list-button list-button-prev']"))
            # filtrmonth_prev.click()

            time.sleep(3)
            above_12 = driver.find_element_by_link_text('до 12:00')
            above_12.click()
            time.sleep(1)
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # переходим вниз станицы, раотает

            time.sleep(1)
            k = 0
            while k < 200:  # чтобы скроллиить к  началу станицы
                scroll = driver.find_element_by_tag_name('body').send_keys(Keys.UP)
                k += 1
            time.sleep(2)


            my_courses = driver.find_element_by_link_text('выходные')
            my_courses.click()
            time.sleep(1)
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # переходим вниз станицы, раотает

            time.sleep(1)
            k = 0
            while k < 200:  # чтобы скроллиить к  началу станицы
                scroll = driver.find_element_by_tag_name('body').send_keys(Keys.UP)
                k += 1
            time.sleep(2)


            posle_18 = driver.find_element_by_link_text('после 18:00')
            posle_18.click()
            time.sleep(1)
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # переходим вниз станицы, раотает

            time.sleep(1)
            k = 0
            while k < 200:  # чтобы скроллиить к  началу станицы
                scroll = driver.find_element_by_tag_name('body').send_keys(Keys.UP)
                k += 1
            time.sleep(2)

            # # жмем на следующий месяц
            # filtr_month_next = WebDriverWait(driver, 10).until(
            #     ec.presence_of_element_located((By.XPATH, "//button[@class='btn list-button list-button-next']")))
            # filtr_month_next.click()

            #time.sleep(2)


            # жмем Любое время
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//a[@class='link']")))[0].click()

            time.sleep(2)

            # жмем Мои курсы:
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH,  "//a[@class='link']")))[5].click()

            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # переходим вниз станицы, раотает
            time.sleep(1)

            k = 0
            while k < 200:  # чтобы скроллиить к  началу станицы
                scroll = driver.find_element_by_tag_name('body').send_keys(Keys.UP)
                k += 1
            time.sleep(2)

            # жмем Любое время
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//a[@class='link']")))[0].click()


            time.sleep(2)

            # выбираем пространство
            time.sleep(3)
            area_button = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//div[@class='value value-with-arrow lm-lg-none']")))

            area_button.click()
            time.sleep(2)

            for i in range(0, 8):# выбираем простантва

                time.sleep(2)
                if i == 6:
                    break
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//label[@class='select-params-item']")))[i+2].click()



    def tear_down(self):

        time.sleep(5)
        self.driver.quit()
            
            
if __name__ == "__main__":
    unittest.main()
                







