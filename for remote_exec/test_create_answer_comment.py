# -*- coding: utf-8 -*-
"""
Created on Sun May 20 17:44:47 2018

@author: usse
WebDriver.implicitly_wait().Метод принимает
            целочисленный
            ввод, который
            определяет, сколько
            секунд
            ждать
            при
            выполнении
            любого
            из
            методов
            find_element.
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
from random import randint
import secrets
from secrets import choice
import string



class Created_comments(unittest.TestCase):

    def authorization(self, driver):  # авторизация

        driver.get('https://admin:LY1R1VMXJ1@dev.leroyfactory.ru')  # чтобы обойти базовую аунтентификацию
        # driver.get("https://dev.leroyfactory.ru/main")

        #кнопка Войти:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH,
                                                 "//a[@class='link link-block']")))[6].click()

        time.sleep(2)
        # атворизуемся
        login = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='login']")))
        login.send_keys("admin@mail.ru")

        time.sleep(2)
        password_d = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']")))
        password_d.send_keys("password")

        time.sleep(2)
        but_send = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class ='btn-green btn signin-submit-button']")))  # отправть
        but_send.click()


    def generation_stroka(self, count_bukv_v_slove, count_slov):

        list_slov = []
        for i in range(0, count_slov):  # цикл по колчиву слов в спике слов

            list_bukv = []
            for j in range(count_bukv_v_slove):  # цикл по буквам
                # print("слоов равно")
                list_bukv.append(' '.join([choice(string.ascii_letters + string.digits)]))

            # print("слово равно", list_bukv )

            list_slov.append(''.join(list_bukv))
        # print(list_slov)

        return str(' '.join(list_slov))



    def comment_k_mk(self, driver): # отсавляем коммент к рандомному  мк:

        time.sleep(2)

        list_cards = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='courses-card-wrapper']"))) # список всех крачоек мк

        rand_index = randint(0,len(list_cards)-1) # генерит индекс мк
        #print("random index od cards mk equal", rand_index, ",count of cards mk equal", len(list_cards))

        driver.execute_script("arguments[0].scrollIntoView(true);",
                                  list_cards[rand_index])  # скриллим к этому элемементу list_cards[rand_index] ПОМОГЛО!!

        time.sleep(2)

        try:
            list_cards[rand_index].click()
        except:
            time.sleep(5)
            list_cards[rand_index].click()


        time.sleep(2)
        comment_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='comment-item btn write-comment-btn']")))

        time.sleep(2)
        # driver.execute_script("arguments[0].scrollIntoView(true);",
        #                       comment_button)  # скриллим к этому элемементу comment_buttonПОМОГЛО!!


        # Здесь он сам скроллит, пожтому не нужно скроллить  сам
        #print("scroll to", comment_button.location['x'],comment_button.location['y'])
        #driver.execute_script("window.scrollTo({},{});".format(comment_button.location['x'], comment_button.location['y']))


        #loc_for_button = comment_button.location
        #loc_for_button['x'] # вывдет корлинату х леовго верзнего угла
        #loc_for_button['x']# вывдет корлинату у леовго верзнего угла

        #driver.execute_script("window.scrollBy(loc_for_button['x'], loc_for_button['x']);")
        time.sleep(2)
        comment_button.click()
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='ql-editor ql-blank']"))).send_keys(self.generation_stroka(randint(3,10), randint(5,10)))
        time.sleep(2)

        # жмемкнопку Отправить
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn send-comment-btn']"))).click()

        time.sleep(10)

        # driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # переходим вниз станицы, раотает


        # нажимаем на кнпоку "Ответить" или "ххОтвет", отвечает на рандомную  правую снизу кнопку ( эта кнопки "Ответить" или "ххОтвет")
        otvetit_buttons = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located(
                (By.XPATH, "//button[@class='btn answer-btn']")))  # список кнопок Ответить

        #print("count of buttons Otvetit+хxOtvet equal", len(otvetit_buttons))

        rand_index_button_otvetit = randint(0, len(otvetit_buttons) - 1)  # выбираем рандомный индекс кнопки Ответить или "ххОтвет"
        #print("random index of button Otvetit/хxOtvet equal", rand_index_button_otvetit)

        if len(otvetit_buttons) == 1:
            otvetit_buttons[rand_index_button_otvetit].click()

        else:
           # driver.execute_script("arguments[0].scrollIntoView(true);", otvetit_buttons[rand_index_button_otvetit])  # скриллим к этому элемементу ideas_cards[rand_index_for_idea] ПОМОГЛО!!
            time.sleep(4)
            otvetit_buttons[rand_index_button_otvetit].click()




        time.sleep(3)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='ql-editor ql-blank']"))).send_keys(
            self.generation_stroka(randint(3, 10), randint(5, 10)))
        time.sleep(2)

        # жмемкнопку Отправить
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn send-comment-btn']"))).click()

        time.sleep(5)

        element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                  "//a[@href='/master-klassy']")))  # код будет ждать 10 секунд до того, как отдаст исключение TimeoutException или если найдет элемент за эти 10 секунд, то вернет его.
        element.click()  # кликаем по ссылке "Обучение"



    def comment_k_event(self, driver):# отсавляем коммент к  событию:


        events_page = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/sobytiya']")))


        try:
            events_page.click()
        except:
            time.sleep(5)
            events_page.click()

        time.sleep(2)

        events_cards = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='events-card-wrapper']"))) # спсиок картчоек событий

        rand_index_for_event = randint(0, len(events_cards)-1) # генерим индекс события
        #print("random index od cards event equal", rand_index_for_event, ",count of cards event equal", len(events_cards))

        driver.execute_script("arguments[0].scrollIntoView(true);",
                              events_cards[rand_index_for_event])  # скриллим к этому элемементу events_cards[rand_index_for_event] ПОМОГЛО!!


        time.sleep(2)

        try:
            events_cards[rand_index_for_event].click()
        except:
            time.sleep(5)
            events_cards[rand_index_for_event].click()

        time.sleep(2)

        comment_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='comment-item btn write-comment-btn']")))

        time.sleep(2)

        # здесь не скролилм, он сам проскролливает к элементу
        # driver.execute_script("arguments[0].scrollIntoView(true);",
        #                        comment_button)  # скриллим к этому элемементу comment_button ПОМОГЛО!!


        #driver.execute_script("window.scrollBy(420, 24);")# скроллит прямо к этому эулменту
        #driver.execute_script("window.scrollTo({},{});".format(comment_button.location['x'], comment_button.location['y']))

        time.sleep(2)
        comment_button.click()
        time.sleep(1)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='ql-editor ql-blank']"))).send_keys(
            self.generation_stroka(randint(3, 10), randint(5, 10)))
        time.sleep(2)


        # жмем кнопку Отправить
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn send-comment-btn']"))).click()

        time.sleep(3)

        # driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # переходим вниз станицы, раотает

        # нажимаем на кнпоку Ответить, отвечает на

        # нажимаем на кнпоку "Ответить" или "ххОтвет", отвечает на рандомную  правую снизу кнопку ( эта кнопки "Ответить" или "ххОтвет")
        otvetit_buttons = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located(
                (By.XPATH, "//button[@class='btn answer-btn']")))  # список кнопок "Ответить" или "ххОтвет"

        #print("count of buttons Otvetit+хxOtvet equal", len(otvetit_buttons))

        rand_index_button_otvetit_or_хxOtvet = randint(0, len(otvetit_buttons) - 1)  # выбираем рандомный индекс кнопки Ответить или "ххОтвет"
        #print("random index of button Otvetit/хxOtvet equal", rand_index_button_otvetit_or_хxOtvet)

        if len(otvetit_buttons) == 1:
            otvetit_buttons[rand_index_button_otvetit_or_хxOtvet].click()

        else:
            driver.execute_script("arguments[0].scrollIntoView(true);", otvetit_buttons[rand_index_button_otvetit_or_хxOtvet])  # скриллим к этому элемементу ideas_cards[rand_index_for_idea] ПОМОГЛО!!
            time.sleep(2)
            otvetit_buttons[rand_index_button_otvetit_or_хxOtvet].click()

        time.sleep(2)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='ql-editor ql-blank']"))).send_keys(
            self.generation_stroka(randint(3, 10), randint(5, 10)))
        time.sleep(2)



        # жмемкнопку Отправить
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn send-comment-btn']"))).click()

        time.sleep(5)


    def comment_k_idea(self, driver):  # отсавляем коммент к идее:

        ideas_page = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/idei']")))

        try:
            ideas_page.click()
        except:
            time.sleep(5)
            ideas_page.click()


        ideas_cards = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='lm-card-wrapper']"))) # список картчоек идей

        rand_index_for_idea = randint(0, len(ideas_cards)-1) # генерим  индекс идеи


        driver.execute_script("arguments[0].scrollIntoView(true);",
                                  ideas_cards[rand_index_for_idea])  # скриллим к этому элемементу ideas_cards[rand_index_for_idea] ПОМОГЛО!!



        time.sleep(2)
        try:
            ideas_cards[rand_index_for_idea].click()

        except:
            time.sleep(4)
            ideas_cards[rand_index_for_idea].click()
        time.sleep(3)

        comment_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='comment-item btn write-comment-btn']")))


        #
        #driver.execute_script("window.scrollBy(420, 24);")  # скроллит прямо к этому эулменту

        time.sleep(2)
        comment_button.click()
        time.sleep(1)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='ql-editor ql-blank']"))).send_keys(
            self.generation_stroka(randint(3, 10), randint(5, 10)))
        time.sleep(2)



        # жмем кнопку Отправить
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn send-comment-btn']"))).click()

        time.sleep(4)

        # driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # переходим вниз станицы, раотает

        # нажимаем на кнпоку "Ответить" или "ххОтвет", отвечает на рандомную  правую снизу кнопку ( эта кнопки "Ответить" или "ххОтвет")
        otvetit_buttons = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn answer-btn']"))) # список кнопок Ответить

        #print("count of buttons Otvetit and Otvet equal", len(otvetit_buttons))

        rand_index_button_otvetit = randint(0, len(otvetit_buttons)-1) # выбираем рандомный индекс кнопки Ответить или "ххОтвет"
        #print("random index of button Otvetit and Otvet equal", rand_index_button_otvetit)


        if len(otvetit_buttons) == 1:
            otvetit_buttons[rand_index_button_otvetit].click()

        else:
            driver.execute_script("arguments[0].scrollIntoView(true);", otvetit_buttons[rand_index_button_otvetit])  # скриллим к этому элемементу ideas_cards[rand_index_for_idea] ПОМОГЛО!!
            time.sleep(2)
            otvetit_buttons[rand_index_button_otvetit].click()




        time.sleep(2)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='ql-editor ql-blank']"))).send_keys(
            self.generation_stroka(randint(3, 10), randint(5, 10)))
        time.sleep(2)


        # жмемкнопку Отправить
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn send-comment-btn']"))).click()

        time.sleep(5)







    def setUp(self):

        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
            "browserName": "chrome",
        })

        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        self.driver.set_window_position(0, 0) # устанавливает позицию левого вурзнего угла окна браузера

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()
        #self.driver.fullscreen_window() # откроет браузер на весь экзан





    def test_created_comments(self):

        driver = self.driver
        self.authorization(driver)  # вызво с регитсрации

        time.sleep(2)
        element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                  "//a[@href='/master-klassy']")))  # код будет ждать 10 секунд до того, как отдаст исключение TimeoutException или если найдет элемент за эти 10 секунд, то вернет его.

        try:
            element.click()# кликаем по ссылке "Обучение"
        except TimeoutError:
            time.sleep(5)
            element.click()  # кликаем по ссылке "Обучение"
            #print("reference is not clickable")  #


        time.sleep(2)
        self.comment_k_mk(driver)# вызов метода котрый выше
        time.sleep(2)
        self.comment_k_event(driver) # вызов метода котрый выше
        time.sleep(2)
        self.comment_k_idea(driver)# вызов метода котрый выше

        time.sleep(5)








    def tear_down(self):
        time.sleep(25)
        #self.driver.quit()
        self.driver.close() # закрывает браузер
        #pass


if __name__ == "__main__":
    unittest.main()

