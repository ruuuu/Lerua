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
class Statistics(unittest.TestCase):


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
        login.send_keys("superadmin@mail.ru")

        time.sleep(2)
        password_d = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']")))
        password_d.send_keys("password")

        time.sleep(2)
        but_send = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class ='btn-green btn signin-submit-button']")))  # отправть
        but_send.click()



    def poisk_in_mk_sattistics(self, driver):

        time.sleep(2)
        # жмем на иконка поиска
        search_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn search-btn']")))
        time.sleep(3)
        search_button.click()

        time.sleep(2)
        result = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск...']")))
        time.sleep(1)
        result.send_keys("мк_мк")
        time.sleep(1)
        result.send_keys(Keys.ENTER)  # нажатие клавиши ентер
        time.sleep(3)

        # нажатие на кнпоку крестик
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn masters-search-query-remove']"))).click()


    def statisitic_events(self, driver):

        time.sleep(2)
        # стаистика по событиям:
        # жмем на Все у собыий
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/profile/superadmin/events']"))).click()

        time.sleep(2)

        # сортировка полей по возратсанию и убыванию:
        up_rows = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn lm-sort-buttons-up']")))

        down_rows = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn lm-sort-buttons-down']")))

        # for i in range(0, len(down_rows)):
        #     time.sleep(1)
        #     up_rows[i].click()
        #     time.sleep(2)
        #     down_rows[i].click()

        time.sleep(2)

        # жмем кнопку предыдущего месяца
        for i in range(0, 5):
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='btn list-button list-button-prev']"))).click()
            time.sleep(2)

        # жмем кнопку следующего месяца
        for i in range(0, 5):
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='btn list-button list-button-next']"))).click()

            time.sleep(2)

        # жмем на  месяц
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn viewport']"))).click()

        time.sleep(2)

        # в попапе перебираем месяцы
        motnts_events = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='month-item']")))

        for i in range(0, len(motnts_events)):
            motnts_events[i].click()
            time.sleep(3)

        time.sleep(2)

        # в апопапе жмем на кнопку предуддущего месяца
        for i in range(0, 5):
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='btn month-prev-btn month-btn-item']"))).click()
            time.sleep(3)

        for i in range(0, 5):  # в апопапе жмем на кнопку следющего  месяца
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='btn month-next-btn month-btn-item']"))).click()
            time.sleep(3)

        self.poisk_in_events_statistics(driver)  # вызов метода поиска в стаитике по соытиям
        time.sleep(2)

        # нажать на кнопку Скачать xlsx
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn download-btn']"))).click()

        time.sleep(3)

        # нажимаем на кнпоку зеденую  Назад  вверху саницы
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-back']"))).click()

        time.sleep(3)



    def statistics_consultations(self, driver):# статситкиа по консультациям:


        # жмем на кнопку Все:
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/profile/superadmin/consultations']"))).click()
        time.sleep(2)

        # пеебираем все протсранства
        areas_for_consultations = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//label[@class='filter-item-wrapper']")))

        for i in range(0, len(areas_for_consultations)):  # проходимся пов сем протсанствам

            areas_for_consultations[i].click()
            time.sleep(2)

        areas_for_consultations[0].click()  # нажатие на Все
        time.sleep(2)

        for i in range(0, 9):  # жмем кнопку предудщего месяца
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn list-button list-button-prev']"))).click()
            time.sleep(2)

        for i in range(0, 9):  # жмем кнопку следующего месяца
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn list-button list-button-next']"))).click()
            time.sleep(2)

        # жмем на сам месяц
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//div[@class='viewport']"))).click()
        time.sleep(1)

        # в календаре жмем кнопку следующего месяца
        for i in range(0, 3):
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn calendar-controls-item calendar-controls-item-right']"))).click()

            time.sleep(2)

        for i in range(0, 3):  # в каледнаре жмем кнопку предыдущего месяца
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn calendar-controls-item calendar-controls-item-left']"))).click()

            time.sleep(2)

        self.poisk_in_consultations_statistics(driver)
        time.sleep(2)

        # жмем кнопку Скачать xlsx
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn download-btn']"))).click()

        time.sleep(2)

        # жмем кнопка Запсиать клента
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn btn-green btn-green-sm add-new-client']"))).click()

        time.sleep(2)
        # жмем кнопку Отмена
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn cancel-btn']"))).click()

        time.sleep(2)
        # жмем кнопку Назад зеленую вверху
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn btn-back']"))).click()




    def statisitic_mk(self, driver):  # статситкиа по мк:


        # жмем на Все у мк
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/profile/superadmin/courses']"))).click()

        areas = WebDriverWait(driver, 10).until(
             ec.presence_of_all_elements_located((By.XPATH, "//label[@class='filter-item-wrapper']")))
        #
        # for i in range(0, len(areas)):  # прохожтимся по всем протсранствам
        #     areas[i].click()
        #     time.sleep(3)

        areas[0].click() #  жмем на Все
        time.sleep(2)

        # сортировка поле по возратсанию и убыванию:
        up_rows = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn lm-sort-buttons-up']")))

        down_rows = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn lm-sort-buttons-down']")))
        print("всего стрелок вниз", len(down_rows))
        print("всего стрелок вверх", len(up_rows))

        # for i in range(0, len(down_rows)):
        #     time.sleep(1)
        #     up_rows[i].click()
        #     time.sleep(2)
        #     down_rows[i].click()

        time.sleep(2)


        self.poisk_in_mk_sattistics(driver) #  вызов метода поиска в стаистике мк

        areas[0].click()  # нажатие на Все
        time.sleep(2)

        # нажимаме на кнпоку 4 раза  епредудыщуго месяца
        for i in range(0, 4):
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn list-button list-button-prev']"))).click()
            time.sleep(3)

        # нажимаме на кнпоку 4 раза   слудующего месяца
        for i in range(0, 4):
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn list-button list-button-next']"))).click()
            time.sleep(3)

        time.sleep(3)

        #  нажимаем на сам месяц
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn viewport']"))).click()

        time.sleep(2)

        months_list = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='month-item']")))

        for i in range(0, len(months_list)): # прохождимся по всем мсяцам конкртного года
            months_list[i].click()
            time.sleep(3)

        time.sleep(3)


        # в попапе нажимаме на кнпоку предудущего месяца
        for i in range(0, 5):
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn month-prev-btn month-btn-item']"))).click()
            time.sleep(2)

        time.sleep(2)

        # в попапе нажимаме на кнпоку следующего месяца
        for i in range(0, 7):
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn month-next-btn month-btn-item']"))).click()
            time.sleep(2)

        time.sleep(2)

        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn viewport']"))).click()

        time.sleep(3)
        # нажимем на кнопку Скачать xlsx
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn download-btn']"))).click()

        time.sleep(3)

        # жмем кнопку Добавить
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//a[@class='link link-inline-block btn-add-idea add-new-client']"))).click()
        time.sleep(2)

        # жмем на крестик
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn lm-creation-header-close-btn']"))).click()
        time.sleep(2)

        # жмем зеделеную еноку Назад ввержху
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn btn-back']"))).click()

    def poisk_in_events_statistics(self, driver):

        time.sleep(2)
        # жмем на иконку поиска
        search_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn search-btn']")))
        time.sleep(3)
        search_button.click()

        time.sleep(2)
        result = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск...']")))
        time.sleep(1)
        result.send_keys("3 дня")
        time.sleep(1)
        result.send_keys(Keys.ENTER)  # нажатие клавиши ентер
        time.sleep(3)

        # нажатие на кнпоку крестик
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn events-search-query-remove']"))).click()



    def poisk_in_consultations_statistics(self, driver):

        time.sleep(2)

        WebDriverWait(driver, 10).until( # жмем на пердудщкю дату
            ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn list-button list-button-prev']"))).click()

        time.sleep(2)
        # жмем на иконку поиска
        search_button = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn search-btn']")))
        time.sleep(3)
        search_button.click()

        time.sleep(2)
        result = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск...']")))
        time.sleep(1)
        result.send_keys("Админ")
        time.sleep(1)
        result.send_keys(Keys.ENTER)  # нажатие клавиши ентер
        time.sleep(3)

        # нажатие на кнпоку крестик
        WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='btn masters-search-query-remove']"))).click()




    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера

        #self.driver.fullscreen_window()  # откроет браузер на весь экзан

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, чтобы подгруздимь элементы



    def test_all_statistics(self):

        driver = self.driver
        self.authorization(driver)  # вызываем метод, котрый выше
        time.sleep(3)

        # нажимаем на кионку профиля супералмина
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/profile']"))).click()
        time.sleep(6)

        # зеленая кнопка Администартор
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@class='link link-block btn btn-green-border']"))).click()

        time.sleep(4)


        self.statisitic_mk(driver) # вызов метода стаистики мк

        time.sleep(1)
        self.statisitic_events(driver) # вызов метода статистики по событиям

        time.sleep(2)
        self.statistics_consultations(driver) #статситкиа по консультациям





        #
        # try:#
        #     WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/oborudovanie']"))).click() #код будет ждать 10 секунд до того, как отдаст исключение TimeoutException или если найдет элемент за эти 10 секунд, то вернет его.
        # except TimeoutError:
        #     pass  # ничего не будет делать
        #

        time.sleep(2)# чтобы посомртеть что происходит







    def tear_down(self):
        time.sleep(5)
        self.driver.quit() # закрывает браузер

if __name__ == "__main__":
    unittest.main()










