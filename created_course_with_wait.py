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
from random import random, randrange, randint
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from random import randint
from secrets import choice
import string


# import pytest


class Created_course(unittest.TestCase):

    def authorization(self, driver):  # авторизация

        driver.get('https://admin:LY1R1VMXJ1@dev.leroyfactory.ru')  # чтобы обойти базовую аунтентификацию
        # driver.get("https://dev.leroyfactory.ru/main")

        #кнопка Войти:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH,
                                                 "//a[@class='link link-block']")))[6].click()

        time.sleep(2)
        # атворизуемся
        login =  WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='login']")))
        login.send_keys("admin@mail.ru")

        time.sleep(2)
        password_d = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']")))
        password_d.send_keys("password")

        time.sleep(2)
        but_send = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,"//button[@class ='btn-green btn signin-submit-button']"))) # отправть
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


    def generating_timesss(self):  # гененрирует время

        x_hours = randint(8, 19)
        x_minutes = randint(0, 60)
        y_hours = randint(9, 20)
        y_minutes = randint(0, 60)
        # print("%H:%M-%H:%M", x_hours, x_minutes, y_hours, y_minutes)

        if x_hours < y_hours:
            return '{0}:{1}-{2}:{3}'.format(x_hours, x_minutes, y_hours, y_hours)
        else:
            return '{0}:{1}-{2}:{3}'.format(y_hours, x_minutes, x_hours, y_hours)




    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна


        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()
        #self.driver.fullscreen_window() # откроет браузер на весь экзан





    def test_created_cours(self):

        driver = self.driver
        self.authorization(driver)  # вызво с регитсрации

        time.sleep(5)

        try:
            element = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/master-klassy']"))) #код будет ждать 10 секунд до того, как отдаст исключение TimeoutException или если найдет элемент за эти 10 секунд, то вернет его.
            element.click()# кликаем по ссылке "Обучение"
        except TimeoutError:

            print("время истекло")  #

        time.sleep(2)

        try: # кнопка Добавить
            add = WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-add-idea']")))
            if add.is_displayed():
                add.click()
        except TimeoutError:
            print("время истекло")

        name_mk = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='title']")))
        name_mk.send_keys("мк test")


        time.sleep(1)

        # главное фото прикрепляем:
        file_dicitionary = {0: "/Users/rufina/Desktop/леруа/1488636263147666156.jpg", 1: "/Users/rufina/Desktop/леруа/orig.jpeg",
                            2: "/Users/rufina/Desktop/леруа/s1200.jpeg", 3: "/Users/rufina/Desktop/леруа/zima13.jpg",
                            4: "/Users/rufina/Desktop/леруа/12326gnHcPlbTVLECrewQp.jpg",
                            5: "/Users/rufina/Desktop/леруа/cavbczeweaahcaa-big.jpg",
                            6: "/Users/rufina/Desktop/леруа/1371106736_67.jpg"}

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-course-creation/div/form/div/div[1]/div[2]/div/app-single-media-picker/label/input"))).send_keys(file_dicitionary[randint(0, len(file_dicitionary) - 1)])

        # описание:
        description = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname='description']")))
        description.send_keys(self.generation_stroka(randint(3,7), randint(4,8)))
        time.sleep(1)

        # выбираем   рандоомное протсранство:
        ind = randint(0, 7)
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//label[@class='radio-group-wrapper']")))[ind].click()

        time.sleep(2)
        # еще раз жмем
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//label[@class='radio-group-wrapper']")))[ind].click()

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//label[@class='radio-group-wrapper']")))[randint(0,7)].click()
        time.sleep(1)

        #стоимость:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='price']"))).send_keys(str(randint(1, 5000)))

        time.sleep(1)

        # колво мест:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='maxCapacity']"))).send_keys(str(randint(3, 200)))

        time.sleep(2)

        # Расписание:  данные генерируются, поэтому словари уже не нужны
        dictionary_date = {0: 35, 1: 78, 2: 121, 3: 164 }
        dictionary_time = {0: "17:00-18:00", 1: "13:00-17:00", 2: "12:00-15:00", 3: "14:00-16:00"}


        # ff = driver.find_elements_by_xpath("//div[@class='date-item-content date-item-content-type-']")[0]
        #
        # print("индекс первого дня равен", ff.get_attribute("class")) # вывдет название класса


        for i in range(0, 4): # будет 4  даты мк

            # нажимаем на календарь:
            calendar = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//span[@class='date-picker-placeholder']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", calendar)  # скриллим к этому элемементу calendar ПОМОГЛО!!
            calendar.click()
            time.sleep(5)

            #нажимаем на правую стрелку (чтоы пеертйи на феварль)
            #WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn calendar-controls-item calendar-controls-item-right']")))[i].click()
            try:
                # выбираем дату
                day = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                    (By.XPATH, "//div[@class='date-item-content date-item-content-type-']"))) # спсиок незадизейбелнных дат

                time.sleep(1)
                time.sleep(4)

                count_day = 0
                for j in range(0, len(day)): # считаем колво активных дат на i ой  итерации
                    if day[j].is_enabled and day[j].is_displayed():
                        count_day += 1

                print("число активных дат на", i, "ой итераци ранво", count_day)

                k = randint(i*(count_day-1), (i+1)*(count_day-1 ))  # индекс рандомной даты, из спсика незадизейбленных дат кликаем рандомный дату
                print("на", i, "ой итерации рандомный индекс даты равен", k)

                day[k].click()

            except TimeoutError:
                print("время выбора даты истекло")




            # вбиваем время:
            time.sleep(1)
            WebDriverWait(driver, 15).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@type='text']")))[i+1].send_keys(self.generating_timesss()) #dictionary_time[i]
            time.sleep(3)

            # выбираем мастера:
            WebDriverWait(driver, 15).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='course-schedule-item-maker']")))[i].click()
            time.sleep(5)
            makers = WebDriverWait(driver, 15).until(
                ec.presence_of_element_located((By.XPATH, "//span[@class='master-select-placeholder']")))

            #print("makers.location равно", makers.location) # {'x': 505, 'y': 1}
            dict_elem = makers.location
            print("dict_elem['x']", dict_elem['x']) # выврдит значение кординаты x
            print("dict_elem['y']", dict_elem['y']) # выврдит значение кординаты y

            #print("makers.location.items() равно", makers.location.items()) # выводит  dict_items([('x', 505), ('y', 1)])

            #driver.execute_script("window.scrollBy(dict_elem['x'], dict_elem['y']);")


            #driver.execute_script("arguments[0].scrollIntoView(true);", makers)  # скриллим к этому элемементу(который не виден) makers ПОМОГЛО!
            time.sleep(4)
            makers.click()
            time.sleep(3)

            masters = WebDriverWait(driver, 20).until(
                ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn master-select-item']")))
            time.sleep(2)

            count_masters = 0  # на i ой итераии считаем сколько мастеров в списке
            for mm in range(0, len(masters)):
                if masters[mm].is_displayed():
                    count_masters += 1

            print("на", i, "ой итерации числом мастеров равно", count_masters)

            k_masters = randint(i * count_masters, (i + 1) * count_masters)  # на iой итреации выбираем арндомный индекс мастера
            print("на", i, "ой итерации  выбираем из интервала (", i * count_masters, ",", (i + 1) * count_masters, ") индекс мастера равен k_masters=", k_masters)
            print()
            time.sleep(2)

            for l in range(0, 5):
                driver.execute_script("arguments[0].scrollIntoView(true);",masters[k_masters])  # скриллим к этому элемементу(который не виден) masters[k] ПОМОГЛО!

            time.sleep(3)
            masters[k_masters].click()

            time.sleep(2)
        # вышли из цикла

        #Резервируем оборудование:
        toggler = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//span[@class='lm-toggle-slider']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", toggler) # скроллим к этому элементу
        time.sleep(2)

        toggler.click()

        dictionary_equipment = {0: 1, 1: 3, 2: 4, 3: 3, 4: 2}
        k = len(range(0, 4)) # len[0,1,2,3]=4
        print("число  датк мк равно ", k)

        time.sleep(3)


        for i in range(0, k+1): # так как k=4 даты поэтому 5=4+1

            time.sleep(2)
            WebDriverWait(driver, 20).until(
                ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск по названию']"))).click()

            time.sleep(2)

            equpmsents = WebDriverWait(driver, 20).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='search-results-item']")))

            list_equipments = []  # будет содержать индексы оборудований
            count_equipmnts = 0  # колво оборудований  в выпадающем спсике

            for eq in range(0, len(equpmsents)):
                list_equipments.append(eq)
                count_equipmnts += 1

            print("число оборудований в выпадающем спсике на", i, "ой итераии аврен", count_equipmnts)
            print("список индексов оборудований на", i, "ой итераии аврен ", list_equipments)

            eq_1 = list_equipments[randint(0, count_equipmnts-1)] #  выбрали индекс  обоудования из спсика  индексов оборудований,         dictionary_equipment[i]
            print("на ", i , "ой итераици индкс выбранного оборудовани яравен", eq_1)


            driver.execute_script("arguments[0].scrollIntoView(true);",
                                  equpmsents[eq_1])  # скриллим к этому элемементу(который не виден)  equpments[eq_1]

            time.sleep(3)
            if equpmsents[eq_1].is_displayed():# если элемент видимый,то
                time.sleep(2)
                equpmsents[eq_1].click()
            else:
                time.sleep(2)
                equpmsents[eq_1].click()






            # выбираем дату:
            WebDriverWait(driver, 20).until(
                    ec.presence_of_element_located((By.XPATH, "//span[@class='date-select-placeholder']"))).click()
            time.sleep(2)



            date = WebDriverWait(driver, 20).until(                                                     #len(range(0, 4))=4- кол-во дат
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='date-select-item']")))[i*len(range(0, 4))+i]   #[i*len(range(0, 4))+2*i]
            time.sleep(2)
            driver.execute_script("arguments[0].scrollIntoView(true);", date)  # скриллим к этому элемементу date ПОМОГЛО!!
            time.sleep(2)
            date.click() # выбрали дату (i=0,1,2,3,4)





         #Матераилы "Дополнителньо оплачитвается": словари эти ужене нужны
        dictionary_material = {0: "Материал1", 1: "Материал2", 2: "Материал3", 3:  "Материал4", 4: "Материал5"}
        dictionary_materila_price = {0: "434", 1: "8", 2: "189", 3:  "54", 4: "57"}

        for i in range(0, 5):

            WebDriverWait(driver, 20).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Добавить материал']")))[i].send_keys(self.generation_stroka(randint(3,6), randint(2,4))) #dictionary_material[i]
            time.sleep(1)

            WebDriverWait(driver, 20).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@type='number']")))[i+2].send_keys(str(randint(10, 2000))) #dictionary_materila_price[i]
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

        file_dicitionary_banner = {0: "/Users/rufina/Desktop/леруа/Metal.jpg", 1: "/Users/rufina/Desktop/леруа/orig.jpeg",
                            2: "/Users/rufina/Desktop/леруа/s1200.jpeg", 3: "/Users/rufina/Desktop/леруа/zima13.jpg",
                            4: "/Users/rufina/Desktop/леруа/12326gnHcPlbTVLECrewQp.jpg",
                            5: "/Users/rufina/Desktop/леруа/cavbczeweaahcaa-big.jpg",
                            6: "/Users/rufina/Desktop/леруа/1371106736_67.jpg"} # выбираем из этого словаря ранднмное фото для главной

        # разместить на главной:
        # переключаем тогглер:
        k = 0
        while k < 10:  # скроллим к материалам
            scroll = driver.find_element_by_tag_name('body').send_keys(
                Keys.END)  # сдвигаем вниз  имитируем нажатие сктрелки вниз
            k += 1
        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-toggle-slider']")))[1].click()
        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-course-creation/div/form/div/div[4]/div/section[3]/div[3]/div/app-single-media-picker/label/input"))).send_keys(file_dicitionary_banner[randint(0, len(file_dicitionary_banner) - 1)])


        # кнопка Добавить:
        # WebDriverWait(driver, 20).until(ec.presence_of_element_located(
        #     (By.XPATH, "//button[@class='btn btn-green btn-green-big-padding']"))).click()  #

        time.sleep(40)

    def tear_down(self):
        time.sleep(25)
        self.driver.quit() #
        #self.driver.close() # закрывает браузер
        #pass


if __name__ == "__main__":
    unittest.main()

