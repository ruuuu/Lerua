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
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


# запись на курс с регитсрауцией вначале   нужно   чтобы среди мк были такие на котрые еще не записа клиент
class Zapis_on_course(unittest.TestCase):

    def registration(self, driver):

        driver.get(
            'https://admin:LY1R1VMXJ1@leroyfactory.ru/')  # чтобы обойти базовую аунтентификацию  # страницйа авторизации

        # кнопка Войти:
        WebDriverWait(driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH,
                                                 "//a[@class='link link-block']")))[6].click()

        # атворизуемся
        login = driver.find_element_by_xpath("//input[@formcontrolname='login']")
        login.send_keys("superadmin@mail.ru")

        password_d = driver.find_element_by_xpath("//input[@formcontrolname='password']")
        password_d.send_keys("J5mmwxN5NeqpX3cd")

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                        "//button[@class ='btn-green btn signin-submit-button']"))).click()

    def poisk(self, driver):

        # жмем конку поиска лупы
        search = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn search-btn']")))
        time.sleep(3)
        search.click()

        time.sleep(2)
        #  в поле поика вбиваем название мк
        result = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//input[@type='search']")))[1]

        result.send_keys("pochtovoe mk")

        time.sleep(2)
        result.send_keys(Keys.ENTER)  # нажатие клавиши ентер

        time.sleep(2)  # кнопка крестик
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn courses-search-query-remove']"))).click()

        time.sleep(3)

    def setUp(self):

        self.driver = self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
                "browserName": "chrome",
            })

        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера

        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, чтобы подгруздимь элементы

    def test_zapis_on_cours(self):

        driver = self.driver

        self.registration(driver)  # вызываем метод, котрый выше

        time.sleep(5)
        # выбираем раздел Обучение:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//a[@href ='/master-klassy']")))[0].click()

        time.sleep(5)  # ждем пока загрузится старница


        # # если ку клиента не введены даты рождения
        # #day = driver.find_element_by_xpath("//input[@formcontrolname='day']")
        # #day.send_keys("07")
        # ##
        # #month = driver.find_element_by_xpath("//input[@formcontrolname='month']")
        # #month.send_keys("07")
        # ##
        # #year = driver.find_element_by_xpath("//input[@formcontrolname='year']")
        # #year.send_keys("1991")


        # на санице всех мк :
        list_mk_cards = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='courses-card-wrapper']")))

       # print(" колво картчоек мк равно", len(list_mk_cards))

        #for j in range(0, len(list_mk_cards)): # прходимся по всем картам мк

        time.sleep(6)

        index_card = randint(0, len(list_mk_cards)-1)
        card = list_mk_cards[index_card]
        #print("номер карты равен", index_card)

        time.sleep(3)
        for i in range(0,5):
            driver.execute_script("arguments[0].scrollIntoView(true);", card)  # скриллим к этому элемементу(который не виден) card ПОМОГЛО!!

        time.sleep(2)
        card.click() # кликаме на карту мк



        time.sleep(5)
        try:
            elem = driver.find_element_by_xpath( # кнопка Перенести
                        "//button[@class='btn lm-registration-action-btn lm-registration-action-btn-move']")

            time.sleep(5)
            elem.click()
            #print("элемент Перенести найден, Записаться не найден")

        except NoSuchElementException: # если нет кнопки Перенести

            elem2 = driver.find_element_by_xpath(  # кнопка Перенести
                        "//button[@class='btn btn-green']")

            time.sleep(5)
            elem2.click()
            #print("эдемнет Записаться найден, Перенести не найден")


        time.sleep(3)
         # список  НЕзадизейбленных таймингов:
        count_other_timings = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//label[@class='course-time-item']")))


        i = 0
        dates = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//td[@itemprop='startDate']")))
        #print("колво дат ранво", len(dates))

        list_nezadizeiblennyh_taimingov = []
        #count_other_timings[i].is_selected() равно False  значит тайминг незадизейблен
        while i < len(dates):   #11 таймингов, 10-ый тайминг послдений

                if count_other_timings[i].is_selected() == False:  # если тайминг незадизейбден  то мы еего индекс заноим в спсиок
                        #print(i, "ый тайминг возвращает ", count_other_timings[i].is_selected())
                        list_nezadizeiblennyh_taimingov.append(i)
                i += 1
                        # count_other_timings[i].click() # кликаме нап ервый попавшийм ся незадизебденный тайминг
                        # break # выход ицикла

        index_nezadizeiblennogo_taiminga = randint(0, len(list_nezadizeiblennyh_taimingov)) # из спсика незадизейбдленных таймингов еберм рандомный
        #print("индекс незадизейбленного  рандоиного тайминга равен ", index_nezadizeiblennogo_taiminga-1, "с номеро карты мк равной", index_card)

        count_other_timings[index_nezadizeiblennogo_taiminga-1].click() # кликаем тайминг выбранный
        time.sleep(4)  # подождеи пока загрзится кнопки




        # кнпока "Записаться":
        zapis_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                               "/html/body/app-root/app-modal/div/div[2]/div/app-modal-enroll-course/div/div[4]/div[2]/button")
                                                                                              ))
        driver.execute_script("arguments[0].scrollIntoView(true);",
                                      zapis_button)  # скриллим к этому элемементу(который не виден)
        time.sleep(2)
        zapis_button.click()



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
        time.sleep(2)
        # жмем Крестик
        WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, "//button[@class='btn lm-modal-close-btn']"))).click()

        time.sleep(5)
        # оказываемся на стание мк

        # нажимаем Отменить
        cancel_button = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, "//button[@class='btn lm-registration-action-btn lm-registration-action-btn-cancel']")))

        time.sleep(3)

        for i in range(0, 5):
                    driver.find_element_by_tag_name('body').send_keys(
                        Keys.PAGE_UP)  #скроллит станицу наверх переходим вверх станицы, работает # скриллим к этому элемементу cancel_button

        time.sleep(3)
        cancel_button.click()

        time.sleep(2)

        # нажимаем на зеленую кнопку Назад вверху страницы
        WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, "//a[@class='link link-inline-block btn btn-back']"))).click()

        time.sleep(3)
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







