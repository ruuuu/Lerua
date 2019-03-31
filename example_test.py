# -*- coding: utf-8 -*-
"""
Created on Sun May  6 19:32:05 2018

@author: usse
"""

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
 
import time
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains # lля сколддинга к нужному элементу импортируем класс ActionChains

#from for_export_authorization import export_Admin_authorization # из файла for_export_authorization.py импортируиеи класс export_Admin_authorization


# import pytest
 # здесь  добавление блюда

class Admin_add_dishs(unittest.TestCase):

    def authorization(self, driver):  # авторизация

        driver.get("https://devadmin.bonration.ru/external/login")
        try:
            email_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']")))  #
            email_field.send_keys("8fzxx1cby0gy@mail.ru")
        except TimeoutError:
            print("время ожидания поля емэйл вышло")

        try:
            password_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']")))
            password_field.send_keys("password3")
        except TimeoutError:
            print("время ожидания поля пароль вышло")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                   "/html/body/app-root/portal-login/div/mat-card/mat-card-content[2]/div/div/div/app-spinner-button/button")))
        if button_voity.is_displayed():  # если кнпока Актвина, то
            button_voity.click()


    def edit_dish(self, driver):
                                                                        #           //*[@id="portal-layout"]/app-dishes/div/div/mat-table/mat-row[1]/mat-cell[1]
         WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//*[@id='portal-layout']/app-dishes/div/div/mat-table/mat-row[1]/mat-cell[1]"))).click()
         time.sleep(4)

         # названеи блюда:
         name_dich = driver.find_element_by_xpath("//input[@placeholder='Название блюда']")
         name_dich.clear() # очищве поле прежде чем его заполнть новыми значеняими
         name_dich.send_keys("кабарне")

         # состаав блюда:
         sostav_dishes = driver.find_element_by_xpath("//input[@placeholder='Состав']")
         sostav_dishes.clear()
         sostav_dishes.send_keys("cjcnfd ghjcnj cjcnfd ,k.lg")

         # колво каллорий блюда:
         cout_caloriy = driver.find_element_by_xpath("//input[@placeholder='Количество калорий (кк)']")
         cout_caloriy.clear()
         cout_caloriy.send_keys("82")

         # вес блюда:
         weight_dishes = driver.find_element_by_xpath("//input[@placeholder='Вес (г)']")
         weight_dishes.clear()
         weight_dishes.send_keys("11")


         WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='btn remove-img-button ng-star-inserted']"))).click()# кнопка крестик на изображении
         driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\usse\\Desktop\\тест_блюда\\rsp.jpg")

         WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"app-spinner-button"))).click() # Сохранить
         time.sleep(4)



    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_admin_dish(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше

        time.sleep(4)  # чтобы сразу окно не закрывалось

        # выбираем пункт "все блюда":                                               "/html/body/app-root/portal-layout-classic/mat-sidenav-container/mat-sidenav[1]/portal-menu-sidenav/div/div/mat-nav-list/a[4]/div/div[2]/h3"
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,  "/html/body/app-root/portal-layout-classic/mat-sidenav-container/mat-sidenav[1]/portal-menu-sidenav/div/div/mat-nav-list/a[4]/div/div[2]/h3"))).click()

        # нажимать на кнопку "Добавить":
        driver.find_element_by_xpath("//*[@id='portal-layout']/app-dishes/div/div/div/div/button").click()

        # наичнаем заполнять форму блюда:
        #  поле "Название блюдо":
        time.sleep(5)
        driver.find_element_by_xpath("//input[@placeholder='Название блюда']").send_keys("блюдо dishes")


        # if (name_dish_filed.get_attribute('value') != ''):
        #
        #     name_dish_filed.clear() # очищае поле если оно не пустое



        #  поле "состав":
        sostav_dish_filed = driver.find_element_by_xpath("//input[@placeholder='Состав']").send_keys("арвар врва варвар варва вар 2 куска сыра")

        # поле Количество калорий:
        driver.find_element_by_xpath("//input[@placeholder='Количество калорий (кк)']").send_keys("230")

        # поле Грамм:
        driver.find_element_by_xpath("//input[@placeholder='Вес (г)']").send_keys("85")

        # прикрепляем файл:
        driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\usse\\Desktop\\тест_блюда\\BinaryImage.jpg")

        # кнопка "Сохранить":
        save_button = driver.find_element_by_xpath("//*[@id='mat-dialog-0']/app-create-dish/div[3]/div[2]/app-spinner-button/button")
        if save_button.is_displayed():# если кнопка видима
            save_button.click()

        time.sleep(8)

        # # выбираем пункт "все блюда":
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,  "/html/body/app-root/portal-layout-classic/mat-sidenav-container/mat-sidenav[1]/portal-menu-sidenav/div/div/mat-nav-list/a[4]/div/div[2]/h3"))).click()

        self.edit_dish(driver)# вызов метода редиактирования блюда, котрый описан выше



    def tear_down(self):
        time.sleep(8)
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



