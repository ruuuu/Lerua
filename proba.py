#
import random
import string
#
import time
import unittest
from random import random, randrange, randint
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from random import randint
from secrets import choice
import string


# class testclass(unittest.TestCase):
#
#
#     def generation_stroka(self, count_bukv_v_slove, count_slov):
#
#         list_slov = []
#         for i in range(0, count_slov):  # цикл по колчиву слов в спике слов
#
#             list_bukv = []
#             for j in range(count_bukv_v_slove):  # цикл по буквам
#                 # print("слоов равно")
#                 list_bukv.append(' '.join([choice(string.ascii_letters + string.digits)]))
#
#             # print("слово равно", list_bukv )
#
#             list_slov.append(''.join(list_bukv))
#         # print(list_slov)
#
#         return str(' '.join(list_slov))
#
#
#     def authorization(self, driver):  # авторизация
#
#         driver.get('https://admin:LY1R1VMXJ1@dev.leroyfactory.ru')  # чтобы обойти базовую аунтентификацию
#         # driver.get("https://dev.leroyfactory.ru/main")
#
#         #кнопка Войти:
#         WebDriverWait(driver, 10).until(
#             ec.presence_of_all_elements_located((By.XPATH,
#                                                  "//a[@class='link link-block']")))[6].click()
#
#         time.sleep(2)
#         # атворизуемся
#         login = driver.find_element_by_xpath("//input[@formcontrolname='login']")
#         login.send_keys(self.generation_stroka(randint(3,10), randint(4,10))
#
#         time.sleep(2)
#         password_d = driver.find_element_by_xpath("//input[@formcontrolname='password']")
#         password_d.send_keys("password")
#
#         time.sleep(2)
#         but_send = driver.find_element_by_xpath("//button[@class ='btn-green btn signin-submit-button']")  # отправть
#         but_send.click()
#
#
#
#
#
#
#     def setUp(self):
#
#         self.driver = webdriver.Chrome()
#         # self.driver = webdriver.Safari()
#         self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
#
#         self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
#
#     def test_method(self):
#         driver = self.driver
#         self.authorization(driver)  # вызываем метод, котрый выше
#
#
#
#
#
#
#     def tear_down(self):
#         time.sleep(30)
#         self.driver.quit()
#
#
#
#
#
# if __name__ == "__main__":
#    unittest.main()


#
# for j in range(9):
#     for i in range(0, 4):
#         N = randint(3, 20)
#
#         for _ in range(N):
#             print(' '.join([choice(string.ascii_letters + string.digits )]), end='') # гененрируте слово из N  букв
#     print(end = ', ')



# print('"', end='')
#kolichestvoslov = randint(3, 25)
#print("число слоов анво", kolichestvoslov)


# def fun_strok():
#
#     N1 = randint(5, 15)# число  слов в предложении
#     print(end='"')
#     for i in range(N1):
#
#         fun_other(randint(3, 10)) # образуем слово
#
#     print('"')
#
# def fun_other(N):
#     #N = randint(3, 10) # генеррирует число буквв  iом слове
#             for _ in range(N):
#                 print(' '.join([choice(string.ascii_letters + string.digits)]), end='') # символ како-йто доин
#             print(end=' ')
#




#my_stroka()






# for i in range(5):
#   bukva = ' '.join([choice(string.ascii_letters + string.digits)]) # букаварандомная
#   list_slov.append(bukva)
#
# print("слово равно", list_slov)

# N1 = randint(5, 15)# число  слов в предложении
# print(end='"')
# for i in range(N1):
#
#     N = randint(3, 10) # генеррирует число буквв  iом слове
#     for _ in range(N):
#         print(' '.join([choice(string.ascii_letters + string.digits)]), end='') # символ како-йто доин
#     print(end=' ')
#
# print('"')



# def hours():
#     x_hours = randint(8, 19)
#     x_minutes = randint(0, 60)
#     y_hours = randint(9, 20)
#     y_minutes = randint(0, 60)
#
#     #print(x_hours,":",x_minutes,"-",y_hours,":", y_minutes)
#
#     if x_hours < y_hours:
#         stroka = x_hours,":",x_minutes,"-",y_hours,":", y_minutes
#         return str(stroka)
#
#     else:
#         stroka = y_hours, ":", x_minutes, "-", x_hours, ":", y_minutes
#         return str(stroka)
#
#
#
# print(hours())



# def generating_timesss():
#
#     x_hours = randint(8, 19)
#     x_minutes = randint(0, 60)
#     y_hours = randint(9, 20)
#     y_minutes = randint(0, 60)
#     #print("%H:%M-%H:%M", x_hours, x_minutes, y_hours, y_minutes)
#
#     if x_hours < y_hours:
#         return '{0}:{1}-{2}:{3}'.format(x_hours, x_minutes, y_hours, y_hours)
#         print(type('{0}:{1}-{2}:{3}'.format(x_hours, x_minutes, y_hours, y_hours)))
#     else:
#         return '{0}:{1}-{2}:{3}'.format(y_hours, x_minutes, x_hours, y_hours)
#         print(type('{0}:{1}-{2}:{3}'.format(y_hours, x_minutes, x_hours, y_hours)))
#
# print(generating_timesss())
#
# # def tel_phone():
# #
#     list_digits = []
#     for i in range(0, 11):
#         if i != 0:
#             #print(string.digits[randint(0,9)]) # 0123456789
#             list_digits.append(string.digits[randint(1,9)])
#
#     #print(list_digits)
#
#     return str(str(8)+''.join(list_digits))

#tel_phone()

# kolichestvoslov = randint(3, 25)
# m = randint(3, 10)
# [print(' '.join(map(str, random.choice(string.ascii_letters + string.digits))), end='')  for i in range(m)  for j in range(kolichestvoslov) for elem in range(9)]





# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:46:56 2018

@author: usse
"""

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support import expected_conditions as ec


# резервирование оборудования с автризацией в начале
class Reserve_equipment(unittest.TestCase):

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

    def setUp(self):

        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()

        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера

        #self.driver.fullscreen_window() # откроет браузер на весь экзан
        # self.driver.implicitly_wait(10) # для  явных ожиданий, чтобы подгруздимь элементы

    def test_reserve_eqipment(self):

        driver = self.driver
        self.authorization(driver)  # вызываем метод, котрый выше
        #
        time.sleep(2)  # ждем пока загрузится старница

        equipment = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href ='/oborudovanie']")))
        equipment.click()


        time.sleep(2)  # ждем пока загрузится старница

        equipment_cards = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class ='lm-card-wrapper']"))) # кликаем конрктено оборудовнаие
        time.sleep(1)



        index = randint(0, len(equipment_cards)) # рандомный индекс карты
        print("random index of cards ravno ",index)
        if equipment_cards[index].is_displayed() is False:
            driver.execute_script("arguments[0].scrollIntoView(true);",
                                  equipment_cards[index])  # скриллим к этому элемементу equipment_cards[index]
            time.sleep(2)
            equipment_cards[index].click()


        else:
            equipment_cards[index].click()


        # for card in range(0, len(equipment_cards)): # проходимся по всем картам оборудований
        #     if equipment_cards[card].is_displayed() is False: # елм карта невидима
        #         driver.execute_script("arguments[0].scrollIntoView(true);",
        #                           equipment_cards[card])  # скриллим к этому элемементу equipment_cards[card]
        #         time.sleep(3)
        #         equipment_cards[card].click()
        #         break# выход из цикла по картам оборудований

        time.sleep(5)  # ждем пока загрузится старница отобрудования


        try: # если есть  # кнопка Резервировать на старнице оборудования
            button_elem = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class ='btn btn-green']")))
            button_elem.click()  # нажатие на эту кнопку
        except:
            # жмем кнопку  зеленую назад:
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@class='link link-inline-block btn btn-back']"))).click()
            time.sleep(3)
            index = randint(0, len(equipment_cards))  # снова рандомный индекс карты
            print("random index of cards ravno ", index)
            if equipment_cards[index].is_displayed() is False:
                driver.execute_script("arguments[0].scrollIntoView(true);",
                                      equipment_cards[index])  # скриллим к этому элемементу equipment_cards[index]
                time.sleep(2)
                equipment_cards[index].click()

            else:
                equipment_cards[index].click()

        time.sleep(5)  # ждем пока загрузится старница резервирования с календарем
        for_me = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,"//label[@class ='lm-radio']")))[1]# Для меня
        for_me.click()


        # список доступных дней
        days = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='date-item-content date-item-content-type-']")))
        print("count of available_days ravno ", len(days))

        rand_index_day = randint(0, len(days)) # рандомный индекс доступного дня
        print("random index of day ravno", rand_index_day)

        days[rand_index_day].click()



        # for i in range(7, 39):
        #
        #     print("i равно", i)
        #     day = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='date-item-wrapper']")))[i]
        #     if day.is_enabled(): # клкаем первую попавшуюся дату активную
        #         print("i равно", i)
        #         day.click()
        #         break



        # for i in range(0, 14): # выбираем рандомный  допустимый атйминг
        #
        #     timing = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='instrument-time-item']")))[i]
        #     if timing.is_displayed():
        #         timing.click()
        #         break


        #
        timings =  WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='instrument-time-item']"))) #список таймингов

        list_index_available_timings = [] # спиок индеосв незадтзейленных таймингов
        count_available_timings = 0

        for tim in range(0, len(timings)): # переираем к ажлый тайминг
            if timings[tim].is_enabled: # если текущий таймнг кликаьъбелен
                list_index_available_timings.append(tim)
                count_available_timings +=1

        print("count od available timings ravno",  count_available_timings)
        print("list of available timings ravno ", list_index_available_timings)

        rand_timing1 = list_index_available_timings[randint(0, count_available_timings-1)] # индека  1-го рандомного таминга
        rand_timing2 = list_index_available_timings[randint(0, count_available_timings - 1)]  # индека 2-го  рандомного таминга
        print("random index raven", rand_timing1, rand_timing2)

        timings[rand_timing1].click()
        time.sleep(2)  #
        timings[rand_timing2].click()

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class ='btn btn-green reserve-instrument-btn']"))).click() # нажатине кнопки Резхервировать


        time.sleep(2)  # ждем пока загрузится станица подтвержения резервирования
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class ='btn btn-link-back ']"))).click() # нажимаем на кнпоку Вернуться на сайт

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/profile']"))).click() #заходим в лк

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//label[@class='sorting-item']")))[3].click()  # выбираем раздел обрудвоание
        time.sleep(1)

        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # переходим вниз станицы, раотает
        time.sleep(5)


    def tear_down(self):

        time.sleep(5)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()











