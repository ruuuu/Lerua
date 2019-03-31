# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:46:56 2018

@author: usse
"""

import time
import unittest
from random import random, randrange, randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # ожидания различных событий
from selenium.webdriver.support.ui import Select # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



# запись на курс с регитсрауцией вначале   нужно   чтобы среди мк были такие на котрые еще не записа клиент
class Zapis_on_course(unittest.TestCase):

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


            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                            "//button[@class ='btn-green btn signin-submit-button']"))).click()


        def poisk(self, driver):

            driver.find_element_by_tag_name('body').send_keys(
                Keys.PAGE_UP)  # скроллит станицу наверх переходим вверх станицы, работает

            # жмем конку поиска лупы
            search = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn search-btn']")))



            search.click()

            time.sleep(2)
            #  в поле поика вбиваем название мк
            result = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@type='search']")))[1]

            result.send_keys("почтовое мк")

            time.sleep(2)
            result.send_keys(Keys.ENTER)  # нажатие клавиши ентер

            time.sleep(2)  # кнопка крестик
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn courses-search-query-remove']"))).click()

            time.sleep(3)


        def setUp(self):

            self.driver = webdriver.Chrome()

            self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
            self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера

            #self.driver.maximize_window()
            #self.driver.implicitly_wait(10) # для  явных ожиданий, чтобы подгруздимь элементы



        def test_zapis_on_cours(self):

            driver = self.driver

            self.registration(driver) # вызываем метод, котрый выше


            time.sleep(5)
            # выбираем раздел Обучение:
            WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//a[@href ='/master-klassy']")))[0].click()

            
            time.sleep(5)# ждем пока загрузится старница



            # выбираем курсна сранице всех мк у котрого на картчокее стьк нпока Запсиаться:
            courses_elems = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH,
                                                     "//button[@class='btn btn-more']")))  # список всех кнопок Записаться у котрых есть кнопка "запсаться" на картчоках




            print("колво  кнопок записаться на карчоках мк", len(courses_elems))

            # записываемся на  рандомное мк у котрого на картчокее сть кнпока "Записаться"
            list_index_buttons = []  # пока пустой список

            for i in range(0, len(courses_elems)):  # #провереям есть ли  у картчоик мk кнопка Зааписатся

                if courses_elems[i].is_enabled():# есди конпока кликабельна
                    list_index_buttons.append(i)  # добавляем  индек  кнпоки  Запсиаться в спсиок

            print("колво кнопока записаться  ", len(list_index_buttons))

            if len(list_index_buttons) == 0:  # если список будет пустой то жмем на следущий месяц
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//button[@class='btn list-button list-button-next']"))).click()
                time.sleep(2)

                for i in range(0, len(courses_elems)):  # здесь же провереям есть ли  у картчоик мк кнопка Зааписатся

                    if courses_elems[i].is_enabled():
                        list_index_buttons.append(i)  # добавляем  индек  кнпоки  Запсиаться в спсиок



            # выбираем любой индекс из спсика индексов
            courses_elems[list_index_buttons[randint(0, len(list_index_buttons) - 1)]].click()  # записываемся на рандомное мк, у которогое сть кнпока Запсиаться на карчтке

            k = list_index_buttons[randint(0, len(list_index_buttons) - 1)]  # запоминаем индекс нкопки котрую выбрали
            print("индекс  выбранной кнопки равен", k)

            time.sleep(5)  # подождеи пока загрзится старница

            # нажимаем на кнопку Назад на станиуе запсии на мк:
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn enroll-course-back-btn']"))).click()

            time.sleep(2)






            # если ку клиента не введены даты рождения
            #day = driver.find_element_by_xpath("//input[@formcontrolname='day']")
            #day.send_keys("07")
            ##
            #month = driver.find_element_by_xpath("//input[@formcontrolname='month']")
            #month.send_keys("07")
            ##
            #year = driver.find_element_by_xpath("//input[@formcontrolname='year']")
            #year.send_keys("1991")
            ##
            ##
            #button_dalee = driver.find_element_by_xpath("//button[@class ='btn btn-more']")# кнопка Далее
            #button_dalee.click()

            time.sleep(5)# подождеи пока загрзится старница


            courses_elems[k].click()  #  cнова нажимаем ЗАПИСАТЬТЬСЯ на картчоке мк,  записываемся на это мк

            print("индекс  кнопки  пвоторного мк равен", k)

            # считаем колв таймингов:
            count_timings = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//label[@class='course-time-item']")))

            for i in range(0, len(count_timings)): # перебираем  все  незадизейбленные тайминги

                button_timing = driver.find_elements_by_xpath("//div[@class ='course-time-item-content']")[i]

                if button_timing.is_enabled(): # если атйминг не задизейбдлин, записываемся на первый незадизейбленный таймиг
                    button_timing.click()
                    break # выходим из цикла

            time.sleep(2)# подождеи пока загрзится кнопки
            # кнпока "Записаться":
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                            "/html/body/app-root/app-modal/div/div[2]/div/app-modal-enroll-course/div/div[4]/div[2]/button")
                                                                               )).click()
            time.sleep(3)
            # кнпока "пригласить друга" на срание подтверждения записи на мк
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                            "//button[@class ='btn btn-invite-friend payment-success-btn']"))).click()
            time.sleep(5)
            # кнопка "поделиться ссылкой": на срание подтверждения записи на мк
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                            "/html/body/app-root/app-modal/div/div[2]/div/app-modal-payment-success/div/div[5]/div[3]/app-share-button/div/button"))).click()
            time.sleep(2)
            # в попапе выбираем "копировать ссылку" на срание подтверждения записи на мк
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                            "//button[@class ='btn popup-icons-item popup-icons-item-copy']")
                                                                           )).click()
            time.sleep(3)
            # кнопка "вернуться на сайт" на срание подтверждения записи на мк
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                            "//button[@class ='btn btn-link-back ']")
                                                                           )).click()
            time.sleep(4)





            self.poisk(driver) # вызываем метод поиска

            time.sleep(2)

            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//a[@href='/profile']"))).click()  # заходим в лк

            time.sleep(2)
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//label[@class='sorting-item']")))[
                1].click()  # выбираем раздел обучение
            time.sleep(1)

            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # переходим вниз станицы, раотает




        def tear_down(self):

            time.sleep(4)
            self.driver.quit()
            

if __name__ == "__main__":
    unittest.main()
    
                            
            




