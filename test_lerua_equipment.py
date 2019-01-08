# -*- coding: utf-8 -*-

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
from selenium.webdriver.common.action_chains import ActionChains # lля сколддинга к нужному элементу импортируем класс ActionChains

# import pytest


class Admin_authorization(unittest.TestCase):


    def authorization(self, driver): # авторизация

        driver.get('https://admin:LY1R1VMXJ1@dev.leroyfactory.ru') #  чтобы обойти базовую аунтентификацию
        #driver.get("https://dev.leroyfactory.ru/main")


        # кнопка Войти:
        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//a[@class='link link-block']" )))[6]
        button_voity.click()

        #  поле Логин
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='login']"))).send_keys("admin@mail.ru")

        #  поле ПАРОЛЬ
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys(
            "password")

        # кнопка Войти в форме авторизации
        voity = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn-green btn signin-submit-button']" )))



        if voity.is_displayed():  # если кнпока видна , то
            voity.click()


    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
            "browserName": "chrome",
        })

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()
        #self.driver.fullscreen_window()  # откроет браузер на весь экзан

    def test_method_add_equipment(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода  авторизации,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось

        # переход к рарделу Оборудование:
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/oborudovanie']"))).click()
        time.sleep(5)

        # кнопка Добавить на станице всех оборудований
        add_button = WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-add-idea']")))

        if add_button.is_displayed():  # если кнпока видна , то
            add_button.click()

        # фото
        WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(
                "/Users/rufina/Desktop/Леруа/Metal.jpg")

        time.sleep(2)

        #  на станце создания оборудования
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='title']"))).send_keys("test equipment")

        time.sleep(2)

        for i in range(0, 9):
            # выбираем пространстов
            if (i == 1 or i == 3 or i == 7 or i == 8):
                WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='radio-group-item']")))[i].click() # металл выбираем




        time.sleep(2)

        for i in range(9, 15):
            # выбираем материал
            if (i == 10 or i == 13):
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//div[@class='radio-group-item']")))[i].click()  #  материал ткань

        time.sleep(2)

        # переходим к элементу Назначение, СКРОЛЛИМ
        #actions = ActionChains(driver)  # создаем объект клааса ActionChains


        # выбираем Назначение
        naznachenie = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='radio-group-item']")))[18] # выбираем Фрезеровать

        driver.execute_script("arguments[0].scrollIntoView(true);", naznachenie)  # скролим к элементу  naznachenie

        time.sleep(2)
        naznachenie.click()

        time.sleep(2)

        # ОПИСАНИЕ
        description = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname='description']"))).send_keys("kfhglkfd dfgkd dfndsk sdgjsdfgd dfgdfgd")
        time.sleep(2)

        dictionary_characterisitic = {0: "characterisitic1", 1: "characterisitic2", 2: "characterisitic3", 3: "characterisitic4", 4: "characterisitic5", 5: "characterisitic6"}
        dictionary_characterisitic_znachenye = {0: "value1", 1: "value2", 2: "value3", 3: "value4", 4: "value5", 5: "value6"}

        # характеристика
        for i in range(0, 6):

            add_characteristic = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn btn-green-plus btn-green-plus-trigger']")))[0]

            driver.execute_script("arguments[0].scrollIntoView(true);", add_characteristic)  # скролим к элементу  add_characteristic

            time.sleep(1)
            add_characteristic.click()

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                (By.XPATH, "//input[@placeholder='Наименование']")))[i].send_keys(dictionary_characterisitic[i])
            time.sleep(1)

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                    (By.XPATH, "//input[@placeholder='Значение']")))[i].send_keys(dictionary_characterisitic_znachenye[i])
            time.sleep(1)

        time.sleep(1)
        #  удаление характеристик
        for i in range(0, 6):

            if (i == 1 or i == 3):
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//button[@class='btn creation-material-remove-btn']")))[i].click()

            time.sleep(1)




        dictionary_materials = {1: "material1", 2: "material2", 3: "material3", 4: "material4", 5: "material5"}
        dictionary_materials_price = {1: "89", 2: "123", 3: "387", 4: "265", 5: "789"}

        for i in range(0, 5):

            # расходные материалы:
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Добавить материал']")))[i].send_keys(dictionary_materials[i+1])
            time.sleep(2)

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                (By.XPATH, "//input[@placeholder='0']")))[i].send_keys(dictionary_materials_price[i+1])
            time.sleep(2)

            if (i == 0 or i == 3 or i == 4):
                at_lerua = driver.find_elements_by_xpath("//div[@class='where-find-item-content where-find-item-content-leroy']")[
                    i]  # в магазине леруа
                driver.execute_script("arguments[0].scrollIntoView(true);", at_lerua)  # скролим к элементу  at_lerua
                at_lerua.click()
                time.sleep(1)
            time.sleep(2)

            if (i == 1 or  i == 2 or i == 4):
                at_fabric = driver.find_elements_by_xpath("//div[@class='where-find-item-content where-find-item-content-fabric']")[
                    i]  # в на фарике
                driver.execute_script("arguments[0].scrollIntoView(true);", at_fabric)  # скролим к элементу  at_fabric
                at_fabric.click()
                time.sleep(1)

        time.sleep(1)
        # удаление материалов:
        for i in range(4, 9):
            if i == 5 :
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//button[@class='btn creation-material-remove-btn']")))[i].click()

        time.sleep(5)

        # КУРСЫ :
        dictionary_name_courses = {6: "course1", 7: "course2", 8: "course3"}
        dictionary_courses_price = {6: "14", 7: "10", 8: "19"}

        for i in range(4, 7):

           add_basic_course =  WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                    (By.XPATH, "//button[@class='btn btn-green-plus btn-green-plus-trigger']")))[1] # зеленая  кнопка "+ Базовый курс"

           driver.execute_script("arguments[0].scrollIntoView(true);", add_basic_course)  # скролим к элементу  toggler
           time.sleep(1)
           add_basic_course.click()
           time.sleep(2)

           WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                    (By.XPATH, "//input[@placeholder='Наименование']")))[i].send_keys(dictionary_name_courses[i+2])
           time.sleep(1)

           WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                    (By.XPATH, "//input[@placeholder='60']")))[i-4].send_keys(dictionary_courses_price[i+2])

           time.sleep(1)


        # Досутп "нужно резервирвоать заранее":
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//span[@class='lm-toggle-slider']"))).click()


        time.sleep(2)

        #  сколько экземпляров оборудования
        time.sleep(1)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='amount']"))).send_keys("3")

        time.sleep(2)
        #Поставщик:
        # Имя
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='provider_name']"))).send_keys("Voscow")

        time.sleep(2)
        #Телефон
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='provider_contact']"))).send_keys(
            "89600345935")

        time.sleep(2)

        # кнопка Добавить:
        # WebDriverWait(driver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-green btn-green-big-padding']"))).click()
        # time.sleep(25)

    def tear_down(self):
        time.sleep(25)
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



