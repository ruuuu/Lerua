# -*- coding: utf-8 -*-
import time

import unittest

from random import random, randrange, randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains # lля сколддинга к нужному элементу импортируем класс ActionChains
from random import randint
from secrets import choice
import string
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


    def generation_tel_phone(self): # генерит номер телфона

        list_digits = []
        for i in range(0, 11):
            if i != 0:
                # print(string.digits[randint(0,9)]) # 0123456789
                list_digits.append(string.digits[randint(1, 9)])

        # print(list_digits)

        return str(str(8) + ''.join(list_digits))


    def my_metho_randem_stroka(self, kolvo_bukv_v_slove, count_slov):

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_bukv = []
            for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

            list_slov.append(''.join(list_bukv))

        return str(' '.join(list_slov))


    def my_metho_with_predlojenie(self, kolvo_bukv_v_slove, count_slov, count_predlojeniy):

        list_predloj = []

        for k in range(count_predlojeniy):  # цикл по колву предло;ений
            list_slov = []
            # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

            for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

                list_bukv = []
                for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                    list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

                list_slov.append(''.join(list_bukv))

            list_predloj.append(' '.join(list_slov) + '.')

        return str(' '.join(list_predloj))





    def setUp(self):


        # self.driver =  self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
        #     "browserName": "chrome",
        # })
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        self.list_characters =  ['A', 'B', 'C', 'D', 'E', 'F', 'G' , 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', '#', '*', '(', ')', '"', ',', '/', ']', '[', '}', '{', '"', '?', '!', '§', '±', '<', '№']


        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


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

        # фото раномное прикрепляем
        file_dicitionary_main = {0: "/Users/rufina/Desktop/lerua/yarkie-kraski-oboi_550x340.jpg",
                                   1: "/Users/rufina/Desktop/lerua/depositphotos_18224999-stock-photo-biotechnology-laboratory-hardware-equipment.jpg",
                                   2: "/Users/rufina/Desktop/lerua/Peyto_Lake-Banff_NP-Canada.jpg",
                                   3: "/Users/rufina/Desktop/lerua/imac-21-5-retina-4k-mne02ua-a-middle-2017.png",
                                   4: "/Users/rufina/Desktop/lerua/nice_pictures_of_the_sea_15.jpg",
                                   5: "/Users/rufina/Desktop/lerua/stanok.jpg",
                                   6: "/Users/rufina/Desktop/lerua/pl16106245-din_32676_sanitary_tri_clamp_fittings_couplings_set_for_food_chemical_pharma_equipments.jpg"}  # выбираем из этого словаря ранднмное фото для главной

        WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file_dicitionary_main[randint(0, len(file_dicitionary_main) - 1)])

        time.sleep(2)

        #  на станце создания оборудования
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='title']"))).send_keys("test_equipment")

        time.sleep(2)


        # выбираем рандомные пространстов randint(0, len(range(0, 9)) - 1)
        for i in range(0, 6): # выберет 5 протснатсва
                                                                                                                                    # len(range(0, 9))=9  берет любое число от 0 до 8
            WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='radio-group-item']")))[randint(0, len(range(0, 9)) - 1)].click() #
            time.sleep(2)

        time.sleep(2)

        #
        for j in range(0, 9): # проходимся по всем пртсранствам , индексы от 0 до 8 вклчительно
            elem = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='radio-group-item']")))[j]
            if elem.is_selected() is False: # если элемнте не выделен
                print(j, "-th element is not selected")
                elem.click()
                break


        count_rand_materials = randint(1,5) # генерирум число материалов

        for i in range(0, count_rand_materials): # выбираем count_rand_materials рандомных  материала, материалы начинаются с 9-го индекса до 14 включительно

            WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//div[@class='radio-group-item']")))[randint(9, len(range(9, 25)) - 2)].click()  #  материал

            time.sleep(2)


        for mat in range(9,15):  # проохдимся по материалам всем, индексы от 9 до 14 включительно
            elem = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='radio-group-item']")))[mat]
            if elem.is_selected() is False: # если элемнте не выделен
                print(mat, "-th element is not selected")
                elem.click()
                break



        # переходим к элементу Назначение, СКРОЛЛИМ
        #actions = ActionChains(driver)  # создаем объект клааса ActionChains
        time.sleep(2)

        naznachenie = WebDriverWait(driver, 10).until(  # берем рандомное число индексы от  15 по 23 вклчительно в
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='radio-group-item']")))



        count_rand_naznachenie = randint(1, 8)  # генерирум число назначений

        # выбираем   count_rand_naznachenie  рандомных Назначений , начинается с 15-го индекса до 23 включительно
        for i in range(0, count_rand_naznachenie):

            n =  randint(15, 23)# генерирует индекс назначения
            print("index of naznachwnia raven", n)

            if n == 23: #Другое
                driver.execute_script("arguments[0].scrollIntoView(true);", naznachenie[n])  # скролим к элементу  naznachenie
                time.sleep(2)
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//div[@class='radio-group-item']")))[n].click()

                time.sleep(2)
                WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Другое назначение']"))).send_keys(self.my_metho_randem_stroka(randint(3,5), randint(4,10)))


            driver.execute_script("arguments[0].scrollIntoView(true);", naznachenie[n])  # скролим к элементу  naznachenie
            time.sleep(2)
            naznachenie[n].click() #

        time.sleep(2)

        for naznach in range(15, 24): # прооиодмся по всем назначениям индексы с 15 по 23  включительно
           elem =  WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='radio-group-item']")))[naznach]

           if elem.is_selected() is False:# если этот элемент не выделен
                elem.click()
                break




        # ОПИСАНИЕ
        description = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname='description']"))).send_keys(self.my_metho_with_predlojenie(randint(4,10), randint(4,15), randint(3,5)))
        time.sleep(2)


        # слвари уже не нужны потмоу чо гененрим данные
        dictionary_characterisitic = {0: "characteristika1", 1: "characteristika2", 2: "characteristika3", 3: "characteristika4", 4: "characteristika5", 5: "characteristika6"}
        dictionary_characterisitic_znachenye = {0: "znachenie1", 1: "znachenie2", 2: "znachenie3", 3: "znachenie4", 4: "znachenie5", 5: "znachenie6"}

        count_characteristic = randint(3, 6) # генерирует число характеристик
        print("count_characteristic ravno", count_characteristic)

        # характеристика
        for i in range(0, count_characteristic):

            add_characteristic = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn btn-green-plus btn-green-plus-trigger']")))[0]

            driver.execute_script("arguments[0].scrollIntoView(true);", add_characteristic)  # скролим к элементу  add_characteristic

            time.sleep(1)
            add_characteristic.click()

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                (By.XPATH, "//input[@placeholder='Наименование']")))[i].send_keys(self.my_metho_randem_stroka(randint(3, 10),randint(4, 9))) #dictionary_characterisitic[i]
            time.sleep(1)

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                    (By.XPATH, "//input[@placeholder='Значение']")))[i].send_keys(self.my_metho_randem_stroka(randint(3, 10),randint(4, 9))) #dictionary_characterisitic_znachenye[i]
            time.sleep(1)

        time.sleep(1)

        # удаляем 0-ую характеристику
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located(
                (By.XPATH, "//button[@class='btn creation-material-remove-btn']")))[0].click()

        ind = i # запониманем последний индекс , снего начнем добавлть курс
        print("поседнйи индекс равен ", ind, i)


        # словар уде нен ужны потому что генерим данные
        #dictionary_materials = {1: "материал1", 2: "материал2", 3: "материал3", 4: "материал4", 5: "материал5"}
        #dictionary_materials_price = {1: "89", 2: "123", 3: "387", 4: "265", 5: "789"}

        N_materials = randint(6, 8) # генерируем числом атериалов
        for i in range(0, N_materials):

            # расходные материалы:
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                (By.XPATH, "//input[@placeholder='Добавить материал']")))[i].send_keys(self.my_metho_randem_stroka(randint(3, 10),randint(4, 9))) #dictionary_materials[i+1]
            time.sleep(2)

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                (By.XPATH, "//input[@placeholder='0']")))[i].send_keys(str(randint(1,400))) #dictionary_materials_price[i+1]
            time.sleep(2)

            if (i == 0 or i == 3 or i == 4):
                at_lerua = driver.find_elements_by_xpath("//div[@class='where-find-item-content where-find-item-content-leroy']")[i]  # в магазине леруа
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
        for i in range(0, N_materials):
            if i == 5 :
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//button[@class='btn creation-material-remove-btn']")))[i].click()

        time.sleep(5)

        # КУРСЫ :
        dictionary_name_courses = {6: "course1", 7: "course2", 8: "course3"}
        dictionary_courses_price = {6: "14", 7: "10", 8: "19"}

        count_course = randint(3, 6) # генеируме колв курсов
        for i in range(ind, ind+count_course):

           add_basic_course =  WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                    (By.XPATH, "//button[@class='btn btn-green-plus btn-green-plus-trigger']")))[1] # зеленая  кнопка "+ Базовый курс"

           driver.execute_script("arguments[0].scrollIntoView(true);", add_basic_course)  # скролим к элементу  toggler
           time.sleep(1)
           add_basic_course.click()
           time.sleep(2)

           WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                    (By.XPATH, "//input[@placeholder='Наименование']")))[i].send_keys(self.my_metho_randem_stroka(randint(4, 8), randint(3, 5))) # dictionary_name_courses[i+2]
           time.sleep(1)

           WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                    (By.XPATH, "//input[@placeholder='60']")))[i-ind].send_keys(str(randint(5, 60))) #dictionary_courses_price[i+2]

           time.sleep(1)


        # Досутп "нужно резервирвоать заранее":
        for k in range(0, 3):
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//span[@class='lm-toggle-slider']"))).click()
            time.sleep(2)

        time.sleep(2)

        #  сколько экземпляров оборудования
        time.sleep(1)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='amount']"))).send_keys(str(randint(1,20)))

        time.sleep(2)
        #Поставщик:
        # Имя
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='provider_name']"))).send_keys(self.my_metho_randem_stroka(randint(3,7), randint(2,5)))

        time.sleep(2)
        #Телефон
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='provider_contact']"))).send_keys(self.generation_tel_phone())

        time.sleep(2)

        # кнопка Добавить:
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-green btn-green-big-padding']"))).click()
        time.sleep(25)

    def tear_down(self):
        time.sleep(25)
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



