# -*- coding: utf-8 -*-
"""
Created on Sat May 12 12:16:53 2018

@author: usse
"""


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
from selenium.webdriver.common.action_chains import ActionChains # lля сколддинга к нужному элементу импортируем класс ActionChains
from random import randint
from secrets import choice
import string

#import pytest


class Create_new_Idea(unittest.TestCase):

    def registration(self, driver):

        driver.get('https://admin:LY1R1VMXJ1@dev.leroyfactory.ru')  # чтобы обойти базовую аунтентификацию
        # driver.get("https://dev.leroyfactory.ru/main")

        # кнопка Войти:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH,
                                                 "//a[@class='link link-block']")))[6].click()

        elem_login = driver.find_element_by_xpath("//input[@formcontrolname='login']")  # у тега input  есть атрибут  formcontrolname со значение login
        elem_login.send_keys("admin@mail.ru")
        elem_password = driver.find_element_by_xpath("//input[@formcontrolname='password']")
        elem_password.send_keys("password")
        button_login = driver.find_element_by_xpath("//*[text()='ВОЙТИ']")  # находит кнопку с надписью 'Войти'
        button_login.click()  # нажатие на эту кнопку


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


    def setUp(self):

        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Safari()
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера

        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, чтобы подгруздимь элементы


    def test_create_on_idea(self):

        driver = self.driver
        self.registration(driver)  # вызываем метод, котрый выше

        time.sleep(8)  # ждем загрузуку всех идей
        block_idea = driver.find_element_by_link_text("Идеи")  # нажимаем на Идеи
        block_idea.click()

        add = WebDriverWait(driver, 18).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-add-idea']")))  # кнопка Добавить
        add.click()

        time.sleep(2)  # ждем пок загруится вся старница


        # главное фото прикрепляем:
        file_dicitionary = {0: "/Users/rufina/Desktop/lerua/Metal.jpg", 1: "/Users/rufina/Desktop/lerua/orig.jpeg",
                            2: "/Users/rufina/Desktop/lerua/s1200.jpeg", 3: "/Users/rufina/Desktop/lerua/zima13.jpg",
                            4: "/Users/rufina/Desktop/lerua/12326gnHcPlbTVLECrewQp.jpg",
                            5: "/Users/rufina/Desktop/lerua/cavbczeweaahcaa-big.jpg",
                            6: "/Users/rufina/Desktop/lerua/1371106736_67.jpg"}

        WebDriverWait(driver, 18).until(ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(
            file_dicitionary[randint(0, len(file_dicitionary) - 1)])

        #название идеи:
        elem = WebDriverWait(driver, 18).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname ='title']" ))) # идет заполняем название идеи
        elem.send_keys("idea")

        time.sleep(1)# краткое описание:
        elem1 = WebDriverWait(driver, 18).until(ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname ='description']" ))) # идет описание идеи
        elem1.send_keys(self.generation_stroka(randint(3,7), randint(4,8)))

        time.sleep(2) #сложность:

        cc = 0
        while cc < 3:
            elem3 = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//label[@class='complexity-setter-item-label']")))[randint(0,2)] #  берем раномноое

            elem3.click()
            time.sleep(2)
            cc += 1

        time.sleep(2)
        # тогглер Нужны спец навыки:
        elem_toggler = WebDriverWait(driver, 18).until(ec.presence_of_element_located((By.XPATH, "//span[@class ='lm-toggle-slider']" )))
        elem_toggler.click()  #

        time.sleep(2)

        #dictionary_for_ability = {1 : "навык1", 2 : "навк2", 3 : "навык3", 4 : "навык4"} # уже не нужно
        for i in range(0, 7): #
            WebDriverWait(driver, 18).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Добавить навык']")))[i].send_keys(self.generation_stroka(randint(3,7), randint(4,8))) #dictionary_for_ability[i+1]
            time.sleep(1)






        time.sleep(2) # время выполнения:
        # переходим к элементу время выполнения, СКРОЛЛИМ
        actions = ActionChains(driver)  # создаем объект клааса ActionChains

        hours = WebDriverWait(driver, 18).until(ec.presence_of_element_located((By.XPATH, "//div[@class='creation-time-picker-type creation-time-picker-type-1']")))
        days = WebDriverWait(driver, 18).until(ec.presence_of_element_located((By.XPATH, "//div[@class='creation-time-picker-type creation-time-picker-type-2']")))
        time.sleep(3)

        elem2 = driver.find_element_by_xpath("//input[@formcontrolname='duration']")  # у тега input есть атрибут duration со значением duration
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              elem2)  # скриллим к этому элемементу(который не виден) calendar
        time.sleep(2)

        elem2.send_keys(str(randint(1, 9)))
        hours.click()
        time.sleep(2)

        days.click()
        time.sleep(2)

        # Материалы:  т к гениеуем тоони уже не ужны
        d_name_materials = {1: "material", 2: "material", 3: "material3"} # словарь для названия материалов
        d = {1: 150, 2: 189, 3: 450} # словарь для значений  полей стоимости

        count_materials = randint(3,7) # генерим колво материалов
        for i in range(0, count_materials):

            add_matearil = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Добавить материал']")))[i]

            #actions.move_to_element(add_matearil).perform()# переходим в к элементу add_matearil не помогло
            # k=0
            # while k < 10:  # скроллим к концу станицы
            #     scroll = driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN) # сдвигаем вниз
            #     k += 1

            # или можно так:
            driver.execute_script("arguments[0].scrollIntoView(true);",
                                      add_matearil)  # скриллим к этому элемементу add_matearil ПОМОГЛО!!
            time.sleep(2)
            add_matearil.send_keys(self.generation_stroka(randint(3,6), randint(1,3))) #" d_name_materials[i + 1]"

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@type='number']")))[i+1].send_keys(str(randint(10, 1000))) #d[i+1]

            time.sleep(2)
            driver.find_elements_by_xpath("//div[@class='where-find-item-content where-find-item-content-fabric']")[i].click()  # на фаьрике

            if i == 1:
                driver.find_elements_by_xpath("//div[@class='where-find-item-content where-find-item-content-leroy']")[
                    i].click()  # в магазине леруа



        time.sleep(2)# тип испольуземых материалов:
        for ch in range(0,4): # 4 раза выберет чекбоксы
            check_box = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='material-types-item']")))[randint(0,4)]

            if check_box.is_displayed() is False: # если элемента нет на санице
                print("check_box is not visible")
                actions.move_to_element(check_box).perform() # скриллим к этому элемементу

            time.sleep(2)
            check_box.click()  #

        for ch in range(0, 5): # проходимся по всем чекбоксам
            check_box = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='material-types-item']")))[ch]

            if check_box.is_selected() is False: # если чекбокс не выелее
                check_box.click()
                break


        time.sleep(2)

        #ИНТСРУМЕНТЫ:
        #dictionary_equipment = {0: 1, 1: 3, 2: 4, 3: 2}
        count_equipments = randint(1, 5) # генерируем числов оборудваоний
        for i in range(0, count_equipments): # выбираем 4 оборудования


            pole = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск по названию']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", pole)  # скриллим к этому элемементу search_elem_1 ПОМОГЛО!!
            pole.click()
            time.sleep(2)

            equipments = WebDriverWait(driver, 20).until(
                ec.presence_of_all_elements_located(
                    (By.XPATH, "//div[@class='search-results-item']")))  # список оборудваний

            print("count of equipments ravno", len(equipments))
            index = randint(0, len(equipments)-1) # генерим индекс оборудования из спсика
            print("index of element equal", index)

            search_elem_1 = equipments[index]
            driver.execute_script("arguments[0].scrollIntoView(true);",
                                  search_elem_1)  # скриллим к этому элемементу search_elem_1 ПОМОГЛО!!
            time.sleep(3)
            search_elem_1.click()

            # WebDriverWait(driver, 20).until(
            #     ec.presence_of_all_elements_located((By.XPATH, "//div[@class='search-results-item']")))[dictionary_equipment[i]].click() # выбрали обоудованеи из спсика

            time.sleep(4)



        # WebDriverWait(driver, 10).until(
        #     ec.presence_of_all_elements_located((By.XPATH, "//div[@class='search-results-item']")))[2].click()  # вбираем из псиска интурумент
        #
        # time.sleep(2) # выбираем втрой интурмент ждем пока загрузится список интрументов
        # search_elem_2 = driver.find_element_by_xpath("//input[@placeholder='Поиск по названию']").click()
        # time.sleep(1)# ждем пока загрузится список интрументов
        # WebDriverWait(driver, 10).until(
        #     ec.presence_of_all_elements_located((By.XPATH, "//div[@class='search-results-item']")))[3].click()  # вбираем из псиска интурумент


        time.sleep(2)

        # загрузка файла перед шагами: добавить



        time.sleep(2)


        # добавляем шаги:
        actions1 = ActionChains(driver)  # создаем объект клааса ActionChains


        # словари эти уже не нужны, та как данные генеририруем
        d_name_step = {1: "step1", 2: "step2", 3: "step3", 4: "step4", 5: "step5", 6: "step6"}
        d_name_step_title = {1: "//input[@id='step-title-1']", 2: "//input[@id='step-title-2']", 3: "//input[@id='step-title-3']", 4: "//input[@id='step-title-4']", 5: "//input[@id='step-title-5']", 6: "//input[@id='step-title-6']"}
        d_name_description_step = {1: "full description of step1", 2: "full description of step2", 3: "full description of step3", 4: "full description of step4"}

        #   фото к  i- му шагу:
        list_images = ["/Users/rufina/Desktop/lerua/Metal.jpg", "/Users/rufina/Desktop/lerua/zima_01.jpg", "/Users/rufina/Desktop/lerua/zima13.jpg",
                       "/Users/rufina/Desktop/lerua/1488636263147666156.jpg", "/Users/rufina/Desktop/lerua/30028592b.jpg",
                        "/Users/rufina/Desktop/lerua/bumaga.jpg", "/Users/rufina/Desktop/lerua/9518959-fractal-flower.jpg", "/Users/rufina/Desktop/lerua/images (1).jpeg", "/Users/rufina/Desktop/lerua/images (2).jpeg",
                       "/Users/rufina/Desktop/lerua/maxresdefault (1).jpg", "/Users/rufina/Desktop/lerua/EN3MDTXxNJU.jpg", "/Users/rufina/Desktop/lerua/kartinka-snegir.jpg", "/Users/rufina/Desktop/lerua/maxresdefault (2).jpg",
                       "/Users/rufina/Desktop/lerua/Ozero--Moreyn-v-Kanade.jpg", "/Users/rufina/Desktop/lerua/moraine3.jpg", "/Users/rufina/Desktop/lerua/s1200.jpeg", "/Users/rufina/Desktop/lerua/stressed-office-worker_23-2147502902.jpg"]
        count_images = len(list_images)
        print(" count_images equal ", count_images)

        # file_dictionary = {1: "/Users/rufina/Desktop/lerua/Metal.jpg", 2: "/Users/rufina/Desktop/lerua/zima_01.jpg",
        #                    3: "/Users/rufina/Desktop/lerua/zima13.jpg", 4: "/Users/rufina/Desktop/lerua/1488636263147666156.jpg ", 5: "/Users/rufina/Desktop/lerua/30028592b.jpg "}

        add_step = driver.find_element_by_xpath("//button[@class='btn btn-red-plus']") # красная кнопка Добавить шаг


        while i < 100: # скроллим к концу станицы
            scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
            i += 1

        count_steps = randint(3, 5) # генеируем колво шагов
        print("count_steps equal = ", count_steps)

        for i in range(0, count_steps): # цикл по шагам

            if i != 0:
              while j < 100: # чтобы скроллиить к  концу станицы
                 scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
                 j += 1

            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, d_name_step_title[i+1]))).send_keys(self.generation_stroka(randint(5,9), randint(4,10)))  # номер шага  d_name_step[i+1]

            time.sleep(2)
            WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//div[@data-placeholder='Введите инструкции']")))[i].send_keys(self.generation_stroka(randint(5,16), randint(25,30)))# опсиание шага d_name_description_step[i+1]

            time.sleep(2)

            for k in range(0, 3): # прикрепляем 3 фото к i-му шагу
                index_file = randint(0, count_images-1)
                print("on ", i, "iteraton  for", k, " foto index_file equal", index_file)

                element_file = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[i+1].send_keys(list_images[index_file]) #file_dictionary[k+1]
                time.sleep(1)

            time.sleep(2)
            # WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            #     (By.XPATH, "//button[@class='btn lm-media-picker-field-add-link']" ))).click() # ссылка на видео
            #
            # time.sleep(2)
            #
            # WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            #         (By.XPATH, "//textarea[@placeholder='Ссылка на видео с YouTube или RuTube']"))).send_keys("https://www.youtube.com/watch?v=pFv8-q0nOcE")

            if i == (count_steps-1): # если это послдерий шаг то выход изз цикла по шалгам
                break

            actions1.move_to_element(add_step).perform()
            actions1.move_to_element(add_step).perform()
            actions1.move_to_element(add_step).perform()
            time.sleep(2)

            driver.execute_script("arguments[0].scrollIntoView(true);", add_step)  # скриллим к этому элемементу add_step ПОМОГЛО!!
            add_step.click()
            time.sleep(2)
            j = 0


         # #   -----------------
         #    WebDriverWait(driver, 10).until(ec.presence_of_element_located(
         #        (By.XPATH, "//input[@id='step-title-1']"))).send_keys("шаг 1") # номер шага
         #
         #    WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
         #        (By.XPATH, "//div[@ data-placeholder='Введите инструкции']")))[0].send_keys("полное описание шага1")# опсиание шага
         #
         #
         #    time.sleep(1)# кнопка Добавить шаг
         #    driver.find_element_by_xpath("//button[@class='btn btn-red-plus']").click()
         #
         #
         #    time.sleep(2)
         #    WebDriverWait(driver, 10).until(ec.presence_of_element_located(
         #        (By.XPATH, "//input[@id='step-title-2']"))).send_keys("шаг 2")# номер шага
         #
         #    WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
         #        (By.XPATH, "//div[@ data-placeholder='Введите инструкции']")))[1].send_keys(
         #        "полное описание шага2")  # опсиание шага

        time.sleep(2)
        add_button = driver.find_element_by_xpath("//button[@class='btn btn-green btn-green-big-padding']")  # кнопка Добавить
        add_button.click()

        time.sleep(30)

        #  Удалить без сохранения
        # remove_button = driver.find_element_by_xpath("/html/body/app-root/app-idea-creation/div/footer/div/div[2]/button") # так не  находит
        # remove_button.click()

    def tear_down(self):
        time.sleep(30)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()




