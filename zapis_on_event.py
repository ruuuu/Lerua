# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:46:56 2018

@author: usse
"""

import time
import unittest

from selenium import webdriver
from random import random, randrange, randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support import expected_conditions as ec

# запись на событие с регитсрауцией вначале

# надо чтобы клиент бал не запсан хотя бы на одно соытие
class Zapis_on_event(unittest.TestCase):

    def registration(self, driver):

        driver.get(
            'https://admin:LY1R1VMXJ1@dev.leroyfactory.ru/')  # чтобы обойти базовую аунтентификацию  # страницйа авторизации

        # кнопка Войти:
        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH,
                                                 "//a[@class='link link-block']")))[6].click()

        # атворизуемся
        login = driver.find_element_by_xpath("//input[@formcontrolname='login']")
        login.send_keys("admin@mail.ru")

        password_d = driver.find_element_by_xpath("//input[@formcontrolname='password']")
        password_d.send_keys("password")

        but_send = driver.find_element_by_xpath("//button[@class ='btn-green btn signin-submit-button']")  # кнопка Отправть
        but_send.click()





    def poisk_and_filter(self, driver):

        # фильтрация  Добавленные мной и  Архив
        for i in range(1, 3):
            time.sleep(2)
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//a[@class='link']")))[i].click()

        time.sleep(2)

        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//a[@class='link']")))[0].click() # Все события

        # жмем конку поиска лупы
        search = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn search-btn']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", search)  # скриллим к этому элемементу
        time.sleep(2)
        search.click()

        time.sleep(2)
        #  в поле поика вбиваем название события
        result = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//input[@type='search']")))[1]


        result.send_keys("zakat")


        time.sleep(2)
        result.send_keys(Keys.ENTER)  # нажатие клавиши ентер

        time.sleep(2) # кнопка крестик
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn events-search-query-remove']"))).click()

        time.sleep(3)




    def setUp(self):

        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера

        # self.driver.implicitly_wait(10) # для  явных ожиданий, чтобы подгруздимь элементы


    def test_zapis_on_event(self):

        driver = self.driver
        self.registration(driver)  # вызываем метод, котрый выше

        time.sleep(5)  # ждем пока загрузится старница
        events = driver.find_element_by_xpath("//a[@href ='/sobytiya']") # выбираем
        events.click()

        time.sleep(5)  # ждем пока загрузится старница всех событий

        events_elems = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn btn-more']"))) # список всех кнопок Записаться у котрых есть кнопка "запсаться" на картчоках



        # # выбираем конкрентное событие:
        # for i in range(0, len(events_elems)):# записываемся на первое попапвшее события у котрого есть кнопка записаться на карточке
        #
        #     if events_elems[i].is_enabled(): #
        #         events_elems[i].click()
        #         break

        # записываемся на  рандомное событие у котрого на картчокее сть кнпока "Записаться"
        list_index_buttons = []# пока пустой список
        for i in range(0, len(events_elems)):# # провереям есть ли  у картчоик событи кнопка Зааписатся

            if events_elems[i].is_enabled():
                list_index_buttons.append(i) # добавляем  индек  кнпоки  Запсиаться в спсиок

        if len(list_index_buttons) == 0:  # если список будет пустой то, то тьс нет кнопко записать на картоках событий

            self.driver.quit() # закрываем ьраузер



        # выбираем любой индекс из спсика индексов
        events_elems[list_index_buttons[randint(0, len(list_index_buttons) - 1)]].click()# записываемся на рандомное событие


        k = list_index_buttons[randint(0, len(list_index_buttons) - 1)] # запонимаем индекс нкопки котрую выбрали
        print("индекс  выбранной кнопки равен", k)


        time.sleep(5)  # подождеи пока загрзится старница

        # нажимаем на кнопку Назад на станиуе запсии на событие:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn enroll-event-back-btn']"))).click()

        time.sleep(2)

        #снова жмем на  кнопку  этого события (на станице всех событий)котрое выбрали:
        events_elems[k].click()
        time.sleep(2)





        #нажимаем на кнпоку "Записаться" yна станице записи на событие:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-modal/div/div[2]/div/app-modal-enroll-event/div/div[2]/div/button"))).click()

        time.sleep(4)
        # кнопка "Пригласить друга" на срание подтвержденяи запсии
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-invite-friend payment-success-btn']"))).click()

        time.sleep(2)
        # кнопка "поделиться ссылкой":
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                        "/html/body/app-root/app-modal/div/div[2]/div/app-modal-payment-success/div/div[5]/div[3]/app-share-button/div/button"))).click()
        time.sleep(2)
        # в попапе выбираем "копировать ссылку"
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                        "//button[@class ='btn popup-icons-item popup-icons-item-copy']")
                                                                       )).click()
        time.sleep(3)
        # кнопка "вернуться на сайт"
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                        "//button[@class ='btn btn-link-back ']")
                                                                       )).click()

        time.sleep(4) # дем пока загрузится станица соьтия




    def tear_down(self):
         #pass
         time.sleep(5)
         self.driver.quit()


if __name__ == "__main__":
    unittest.main()







