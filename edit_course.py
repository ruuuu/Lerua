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



# import pytest


class Edit_course(unittest.TestCase):

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
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()
        #self.driver.fullscreen_window() # откроет браузер на весь экзан





    def test_edit_cours(self): # метод теста  всегда должен начинаться  со слова test

        driver = self.driver
        self.authorization(driver)  # вызво с регитсрации

        time.sleep(2)

        try:
            element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/master-klassy']"))) #код будет ждать 10 секунд до того, как отдаст исключение TimeoutException или если найдет элемент за эти 10 секунд, то вернет его.
            element.click()# кликаем по ссылке "Обучение"
        except TimeoutError:

            print("время истекло")  #

        time.sleep(2)

        # try: # кнопка Добавить
        #     add = WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-add-idea']")))
        #     if add.is_displayed():
        #         add.click()
        # except TimeoutError:
        #     print("время истекло")

        # выбиаем мк:
        master_class = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/master-klassy/dlya-registraciy-479']")))
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              master_class)  # скриллим к этому элемементу master_class ПОМОГЛО!!



        time.sleep(2)
        master_class.click()
        time.sleep(2)

        # нажатие на кнпоку Редактивоать
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn lm-event-action-btn lm-event-action-btn-edit']"))).click()


        name_mk = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='title']")))
        name_mk.send_keys("отредаткированный мк")

        element.clear() # lkz jxbncrb gjktq

        time.sleep(1)
        #главное фото:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-course-creation/div/form/div/div[1]/div[2]/div/app-single-media-picker/label/input"))).send_keys("/Users/rufina/Desktop/Леруа/zima13.jpg")

        # описание:
        description = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname='description']")))
        description.send_keys("описание мк ,jkmijt jgbfybt vr описание мк ,jkmijt jgbfybt vrописание мк ,jkmijt jgbfybt vrописание мк ,jkmijt jgbfybt vrописание мк ,jkmijt jgbfybt vr")

        time.sleep(1)
        # выбираем протсранство:
        for i in range(0, 8):
            if i == 3:
                WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//label[@class='radio-group-wrapper']")))[i].click()

        time.sleep(1)
        #стоимость:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='price']"))).send_keys("678")

        time.sleep(1)
        # колво мест:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='maxCapacity']"))).send_keys("6")

        time.sleep(2)
        # Расписание:
        dictionary_date = {0: 35, 1: 76, 2: 116, 3: 156 , 4:  206}
        dictionary_time = {0: "10:00-11:00", 1: "13:00-17:00", 2: "12:00-15:00", 3: "14:00-16:00", 4: "17:00-19:00"}

        for i in range(0, 5):

            # нажимаем на календарь:
            calendar = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//span[@class='date-picker-placeholder']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", calendar)  # скриллим к этому элемементу calendar ПОМОГЛО!!
            calendar.click()
            time.sleep(3)
            try:
                # выбираем дату
                day = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//div[@class='date-item-wrapper']")))[dictionary_date[i]]
                time.sleep(1)
                day.click()
                # if day.is_displayed():
                #     day.click()

            except TimeoutError:
                print("время выбора даты истекло")



            # вбиваем время:
            time.sleep(1)
            WebDriverWait(driver, 15).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@type='text']")))[i+1].send_keys(dictionary_time[i])
            time.sleep(2)
            # выбираем мастера:
            WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.XPATH, "//span[@class='master-select-placeholder']"))).click()
            time.sleep(2)

            # # выбираем Админ Админов:
            # if i == 2:
            #     WebDriverWait(driver, 20).until(
            #         ec.presence_of_all_elements_located((By.XPATH, "//div[@class='master-select-item']")))[21].click()  # Выбираем мастера
            #     break


            WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='master-select-item']")))[i*14 + i+1].click() # Выбираем Админ админов





        time.sleep(2)
        #Резервируем оборудование:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//span[@class='lm-toggle-slider']"))).click()

        dictionary_equipment = {0: 1, 1: 3, 2: 4 }
        for i in range(0, 3): # будт три оборудования

            time.sleep(2)
            WebDriverWait(driver, 20).until(
                ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск по названию']"))).click()

            time.sleep(1)


            eq_1 = WebDriverWait(driver, 20).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='search-results-item']")))[dictionary_equipment[i]] #выбрали обоудованеи из спсика
                #if eq_1.is_displayed():# если элемент видимый,то
            time.sleep(1)
            eq_1.click()

            # выбираем дату:
            WebDriverWait(driver, 20).until(
                    ec.presence_of_element_located((By.XPATH, "//span[@class='date-select-placeholder']"))).click()
            time.sleep(1)



            date = WebDriverWait(driver, 20).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='date-select-item']")))[i*6+i+1]
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView(true);", date)  # скриллим к этому элемементу calendar ПОМОГЛО!!
            date.click() # выбрали дату (i=0,1,2,3,4)





         #Матераилы:
        dictionary_material = {0: "Материал1", 1: "Материал2", 2: "Материал3", 3:  "Материал4", 4:"Материал5"}
        dictionary_materila_price = {0: "434", 1: "8", 2: "189", 3:  "54", 4:"57"}

        for i in range(0, 5):

            WebDriverWait(driver, 20).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Добавить материал']")))[i].send_keys(dictionary_material[i])
            time.sleep(1)

            WebDriverWait(driver, 20).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@type='number']")))[i+2].send_keys(dictionary_materila_price[i])
            time.sleep(1)

            if (i == 0 or i == 2):
                WebDriverWait(driver, 20).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//div[@class='where-find-item-content where-find-item-content-fabric']")))[i].click()

            WebDriverWait(driver, 20).until(
                ec.presence_of_all_elements_located(
                    (By.XPATH, "//div[@class='where-find-item-content where-find-item-content-leroy']")))[i].click()




        # Фото с  занятий (4 фотки прикрепляем):
        dicrionary_foto = {1: "/Users/rufina/Desktop/Леруа/i.jpeg", 2: "/Users/rufina/Desktop/Леруа/zima13.jpg", 3: "/Users/rufina/Desktop/Леруа/zima_01.jpg", 4: "/Users/rufina/Desktop/Леруа/orig.jpeg"}
        # for i in range(0, 4):
        #     WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[i].send_keys(dicrionary_foto[i+1]) #
        #     time.sleep(1)

        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH,
                                            "/html/body/app-root/app-course-creation/div/form/div/div[4]/div/section[2]/div[2]/div/div[1]/div/div/app-single-media-picker/label/input"))).send_keys(
            "/Users/rufina/Desktop/Леруа/zima13.jpg")

        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH,
                                            "/html/body/app-root/app-course-creation/div/form/div/div[4]/div/section[2]/div[2]/div/div[2]/div/div/app-single-media-picker/label/input"))).send_keys(
            "/Users/rufina/Desktop/Леруа/i.jpeg")

        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH,
                                            "/html/body/app-root/app-course-creation/div/form/div/div[4]/div/section[2]/div[2]/div/div[3]/div/div/app-single-media-picker/label/input"))).send_keys(
            "/Users/rufina/Desktop/Леруа/zima_01.jpg")

        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH,
                                            "/html/body/app-root/app-course-creation/div/form/div/div[4]/div/section[2]/div[2]/div/div[4]/div/div/app-single-media-picker/label/input"))).send_keys(
            "/Users/rufina/Desktop/Леруа/orig.jpeg")



        # ссылка на фотки :
        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='albumUrl']"))).send_keys("https://vk.com/page-87938575_51386471")

        time.sleep(1)

        # разместить на главной:
        # переключаем тогглер:
        k = 0
        while k < 10:  # скроллим к материалам
            scroll = driver.find_element_by_tag_name('body').send_keys(
                Keys.END)  # сдвигаем вниз  имитируем нажатие сктрелки вниз
            k += 1
        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-toggle-slider']")))[1].click()
        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-course-creation/div/form/div/div[4]/div/section[3]/div[3]/div/app-single-media-picker/label/input"))).send_keys("/Users/rufina/Desktop/Леруа/zima13.jpg")


        # кнопка Сохраить:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn btn-green btn-green-big-padding']"))).click()  #

        time.sleep(25)

    def tear_down(self):
        time.sleep(25)
        #self.driver.quit() # закрывает весь браузер
        self.driver.close() # закрывает вкладку
        #pass


if __name__ == "__main__":
    unittest.main()



