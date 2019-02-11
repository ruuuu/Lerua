# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:46:56 2018

@author: usse
"""

import time
from random import random, randrange, randint
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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import base64
from random import randint
from secrets import choice
import string


# созданеи события с регитсрауцией в начале
class Create_event_with_wait(unittest.TestCase):


    def authorization(self, driver):  # авторизация

        # для FF чтобы обойти бозов аунтентификацию
        # aunthentification_token = str("Basic " + base64.b64encode(b'admin:LY1R1VMXJ1'))
        #
        # capa = DesiredCapabilities.PHANTOMJS
        # capa['phantomjs.page.customHeaders.Authorization'] = aunthentification_token
        # driver = webdriver.PhantomJS(desired_capabilities=capa)

        driver.get('https://admin:LY1R1VMXJ1@dev.leroyfactory.ru')  # чтобы обойти базовую аунтентификацию
        #driver.get("https://dev.leroyfactory.ru/main")

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

        self.driver = webdriver.Chrome()    #Firefox()
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна


        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, чтобы подгруздимь элементы



    def test_create_event(self):

        driver = self.driver
        self.authorization(driver)  # вызываем метод, котрый выше
        time.sleep(6)
        #
        try:# кликаем по ссылуе "Событие"
            element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/sobytiya']"))) #код будет ждать 10 секунд до того, как отдаст исключение TimeoutException или если найдет элемент за эти 10 секунд, то вернет его.
            element.click()
        except TimeoutError: # TimeoutException
            pass  # ничегон е будет делать


        time.sleep(3)# чтобы посомртеть что происходит

        try: # кнопа Добавить:
            add = WebDriverWait(driver, 18).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-add-idea']")))
            add.click()
        except TimeoutError:
            pass

        time.sleep(2)

        # главное фото прикрепляем:
        file_dicitionary = {0: "/Users/rufina/Desktop/леруа/Metal.jpg", 1: "/Users/rufina/Desktop/леруа/orig.jpeg",
                            2: "/Users/rufina/Desktop/леруа/s1200.jpeg", 3: "/Users/rufina/Desktop/леруа/zima13.jpg",
                            4: "/Users/rufina/Desktop/леруа/12326gnHcPlbTVLECrewQp.jpg", 5: "/Users/rufina/Desktop/леруа/cavbczeweaahcaa-big.jpg",
                            6: "/Users/rufina/Desktop/леруа/1371106736_67.jpg"}

        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[
            0].send_keys(file_dicitionary[randint(0, len(file_dicitionary) - 1)]) # вставляет рандомную картинку из словаря

            #send_keys("/Users/rufina/Desktop/Леруа/Metal.jpg")  #


        name_event = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='title']")))
        name_event.send_keys("самое длинное событие")

        #  ОРГАНИЗАТОРЫ радиокнпока (на ФАБРИКЕ  тоит по умолчанию)
        time.sleep(2)

        # жмем на радиокнопку:
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='lm-radio-indicator']")))[1].click()
        time.sleep(2)



        #лого:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,
                                                                        "/html/body/app-root/app-event-creation/div/form/div/div[1]/div/section[2]/div[4]/div/div[1]/div[1]/app-logo-picker/label/input"))).send_keys(
                "/Users/rufina/Desktop/Леруа/idea_1920.jpg")  #


        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                    (By.XPATH, "//input[@placeholder='Название']"))).send_keys(self.generation_stroka(randint(3,10), randint(3,10)))

        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                    (By.XPATH, "//input[@placeholder='https://']"))).send_keys("https://automated-testing.info/t/kak-opredelit-klikabelnost-elementa-na-stranicze-s-pomoshhyu-webdriver/3719/18")

        doctinary_foto_f = {1: "/Users/rufina/Desktop/Леруа/zima13.jpg", 2: "/Users/rufina/Desktop/Леруа/zima_01.jpg"}

        dicitionary_name_organizations = {1:self.generation_stroka(randint(3,10), randint(3,10)), 2: self.generation_stroka(randint(3,10), randint(3,10))}

        dicitionary_url = {1: "https://vk.com", 2: "https://facebook.com"}

        dicitionary_xpath = {1: "/html/body/app-root/app-event-creation/div/form/div/div[1]/div/section[2]/div[4]/div/div[2]/div[1]/app-logo-picker/label/input",
                           2: "/html/body/app-root/app-event-creation/div/form/div/div[1]/div/section[2]/div[4]/div/div[3]/div[1]/app-logo-picker/label/input"
                           }

        for i in range(1, 3):
            # зеленая кнопка Добавить
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn btn-green-plus']"))).click()
            # лого:
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, dicitionary_xpath[i]))).send_keys(doctinary_foto_f[i])

            WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                             (By.XPATH, "//input[@placeholder='Название']")))[i].send_keys(dicitionary_name_organizations[i])

            WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                    (By.XPATH, "//input[@placeholder='https://']")))[i].send_keys(dicitionary_url[i])
            time.sleep(2)



        time.sleep(2)






        # краткое описание:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='shortDescription']"))).send_keys(self.generation_stroka(randint(3, 10), randint(3, 10)))
        time.sleep(2)

        #  Основное опсиание:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,
             "//textarea[@formcontrolname='mainDescription']"))).send_keys(self.generation_stroka(randint(3, 10), randint(3, 10)))

        time.sleep(2)
        # программа:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,
             "//textarea[@formcontrolname='program']"))).send_keys(self.generation_stroka(randint(3, 10), randint(3, 10)))
        time.sleep(2)

        # ссылка на программу:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,
             "//input[@formcontrolname='eventPageUrl']"))).send_keys("https://fkjgkdfg.com")

        time.sleep(4)



        # нажатие на календарь(для даты начвла):
        calendar = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//span[@class='date-picker-placeholder']")))[0]

        #actions = ActionChains(driver)  # создаем объект клааса ActionChains
        #actions.move_to_element(calendar).perform()  # скриллим к этому элемементу
        driver.execute_script("arguments[0].scrollIntoView(true);", calendar) # скриллим к этому элемементу calendar ПОМОГЛО!!
        time.sleep(2)
        calendar.click()

        # можно выбирать дпервую попавшуюся незадизейбленные даты:
        time.sleep(8)
        day_1_1 =  WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='date-item-content date-item-content-type-']")))

        count_days_1 = 0  # число незадизейбелнных дат первогок аленаря
        list_day_1 = []

        for i in range(0, len(day_1_1)):  # выбираем первую незадизейбленную дату

            if day_1_1[i].is_enabled() and day_1_1[i].is_displayed():  # если дата незадизейблина

                  list_day_1.append(i)
                  count_days_1 += 1



        #выбираем рандомный индекс из спсика активных дат:
        k1 = randint(0, count_days_1 - 1)
        print("рандомный индекс из спсика активных дат", k1-1)
        day_1_1[list_day_1[k1]].click()



        # for i in range(0, len(day_1_1)): #
        #          if day_1_1[i].is_enabled():  # если дата незадизейблина
        #         time.sleep(3)
        #         #print("day_1_1.is_enabled() возвращает", day_1_1[i].is_enabled(), "i равно", i)
        #         day_1_1[i].click()
        #         break


        time.sleep(4)

        j = k1 # сохраняем индекс  первой даты, чтоыб потмо отталкитьвася длт нее для выбора втрой даты
        # нажатие на календарь(для даты конца):

        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//span[@class='date-picker-placeholder']")))[0].click()

        time.sleep(2)

        day_1_2 = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='date-item-content date-item-content-type-']")))

        # выбираем день:
        for i in range(j+19, len(day_1_2)):  # выбираем прую попавщуюся незадизейбленную дату

            if day_1_2[i].is_enabled():  # если дата незадизейблина
                time.sleep(3)
                print("day_1_2.is_enabled() возвращает", day_1_2[i].is_enabled(), "i равно", i)
                day_1_2[i].click()
                break

        time.sleep(4)

        # можно выбирать из активнх дат рандомные:
        # time.sleep(5)
        # day_1_1 = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
        #     (By.XPATH, "//div[@class='date-item-content date-item-content-type-']")))
        #
        # list_day_1 = []  # здесь будем хранить индексы активныx(не задзейбленные) первыx  дат
        # count_days_1 = 0  # число незадизейбелнных дат первогок аленаря
        #
        # for i in range(0, len(day_1_1)):  # выбираем первую незадизейбленную дату
        #
        #     if day_1_1[i].is_enabled() and day_1_1[i].is_displayed():  # если дата незадизейблина
        #
        #         list_day_1.append(i)
        #         count_days_1 += 1
        #
        # print("list_day_1=", list_day_1)
        #
        # time.sleep(2)
        # print("число незадизейбленных дат первого каленаря", count_days_1)
        #
        # # выбираем рандомный индекс из спсика активных дат:
        # k1 = randint(0, count_days_1 - 1)
        # print("рандомные индекс из спсика активных дат", k1-1)
        # day_1_1[list_day_1[k1]].click()
        #
        # time.sleep(2)
        #
        # # нажатие на календарь(для даты конца):
        #
        # WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
        #     (By.XPATH, "//span[@class='date-picker-placeholder']")))[0].click()
        #
        # time.sleep(2)
        #
        #
        #
        # list_day_2 = []  # здесь будем хранить индексы активныx(не задзейбленные) вторых  дат
        #
        # count_days_2 = 0  # число незадизейбелнных дат второго каленаря
        #
        # print("count of available days 2th calendare", len())
        # # выбираем день:
        # for i in range(18+k1, len(day_1_1) ):  # выбираем  незадизейбленную дату
        #
        #
        #
        # print("list_day_2=", list_day_2)
        #
        # time.sleep(2)
        # print("число незадизейбленных дат второго каленаря", count_days_2)
        #
        # # выбираем рандомный индекс из спсика активных дат:
        # k2 = randint(0, count_days_2 - 1)  #
        # print("рандомный индекс из спсика активных дат", k2-1)


        time.sleep(2)

        # выбираем время:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located( # генерирруем время
            (By.XPATH,
             "//input[@formcontrolname='time']"))).send_keys(self.generating_timesss()) #str('{0}:{1}-{2}:{3}'.format(randint(8, 19), randint(0, 60), randint(9, 20), randint(0, 60)))

        time.sleep(4)

        # место проведения:

        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='lm-radio-indicator']")))[3].click()

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='placeAddress']"))).send_keys(self.generation_stroka(randint(5,8), randint(6,15)))


        # радиокнопка  Стоимость:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,
             "//input[@formcontrolname='price']"))).send_keys(str(randint(1, 2000))) # гнерируте люьое числов  указзанных пределах

        time.sleep(2)

        # указываем колво человек:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,
             "//input[@formcontrolname='maxCapacity']"))).send_keys(str(randint(1, 100)))

        time.sleep(2)

        # указываем ссылку на регитсрацию:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='registrationUrl']"))).send_keys("https://kgjhlkfjhlfjg.com") #

        time.sleep(2)

        # возрастное ограничение:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//label[@class='radio-group-wrapper']")))[randint(0, 4)].click() # выбирате андомное индекс

        time.sleep(2)

        # прикрепляем фото (4 штуки)
        dictoinary_fotos = {1: "/Users/rufina/Desktop/Леруа/zima_01.jpg", 2: "/Users/rufina/Desktop/Леруа/orig.jpeg", 3: "/Users/rufina/Desktop/Леруа/kartinka-snegir.jpg", 4: "/Users/rufina/Desktop/Леруа/zima13.jpg"}

        # for i in range(1, 5):
        #
        #     time.sleep(2) #
        #WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[i].send_keys(dictoinary_fotos[i-1])  #

        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/app-event-creation/div/form/div/div[3]/div/section[2]/div[2]/div/div[1]/div/div/app-single-media-picker/label/input"))).send_keys("/Users/rufina/Desktop/Леруа/images.jpeg")  #
        time.sleep(2)
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-event-creation/div/form/div/div[3]/div/section[2]/div[2]/div/div[2]/div/div/app-single-media-picker/label/input"))).send_keys("/Users/rufina/Desktop/Леруа/zima13.jpg")  #
        time.sleep(2)
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-event-creation/div/form/div/div[3]/div/section[2]/div[2]/div/div[3]/div/div/app-single-media-picker/label/input"))).send_keys("/Users/rufina/Desktop/Леруа/i.jpeg")  #
        time.sleep(2)
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-event-creation/div/form/div/div[3]/div/section[2]/div[2]/div/div[4]/div/div/app-single-media-picker/label/input"))).send_keys("/Users/rufina/Desktop/Леруа/idea_1920.jpg")  #



        # ссылка на фотоаьюбом
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname = 'albumUrl']"))).send_keys("https://vk.com/public42564857") #

        time.sleep(2)

        # Адрес
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname = 'address']"))).send_keys(self.generation_stroka(randint(3,7), randint(2,4))) #

        time.sleep(2)

        # Телефон
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname = 'phone']"))).send_keys(self.generation_tel_phone()) #

        time.sleep(2)

        # Email

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname = 'email']"))).send_keys("ituroiu@ya.ru") #
        time.sleep(5)



        # element_file1 = driver.find_element(by=By.XPATH, value="")  # берем элемент input type='file'
        # element_file1.send_keys("C:\\Users\\usse\\Desktop\\для теста_Леруа\\dog.jpg")
        # time.sleep(6)




        time.sleep(2)

        # мессенждеры:
        #fb:
        add_messanger = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-green-plus btn-green-plus-trigger']")))

        driver.execute_script("arguments[0].scrollIntoView(true);", add_messanger) #скролим к кнопке  add_messanger
        time.sleep(2)
        add_messanger.click()

        time.sleep(1)
        WebDriverWait(driver, 20).until(ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='btn social-types-item lm-social-facebook']"))).click()
        WebDriverWait(driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='https://facebook.com/...']"))).send_keys("https://www.facebook.com/pages/category/Community/%D0%9A%D1%80%D0%B0%D1%81%D0%B8%D0%B2%D1%8B%D0%B5-%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-344648422268527/")

        time.sleep(2)
        #watsup:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located( # зеленая вкнопка Плюс
            (By.XPATH, "//button[@class='btn btn-green-plus btn-green-plus-trigger']"))).click()
        WebDriverWait(driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn social-types-item lm-social-whatsapp']"))).click()
        WebDriverWait(driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='+7 (000) 123 45 67']"))).send_keys("89765437865")

        time.sleep(2)
        #twitter:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn btn-green-plus btn-green-plus-trigger']"))).click()
        WebDriverWait(driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn social-types-item lm-social-twitter']"))).click()
        WebDriverWait(driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='https://twitter.com/...']"))).send_keys("https://twitter.com/alexey_pushkov")

        time.sleep(2)


        # сделать баннер:
        # переключаем тогглер:
        toggler = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-toggle-slider']")))[1]

        driver.execute_script("arguments[0].scrollIntoView(true);", toggler)  # скролим к элементу  toggler
        time.sleep(1)
        toggler.click()

        time.sleep(1)
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-event-creation/div/form/div/div[3]/div/section[5]/div[3]/div/app-single-media-picker/label/input"))).send_keys("/Users/rufina/Desktop/Леруа/idea_1920.jpg")

        driver.find_element_by_xpath("//button[@class='btn btn-green btn-green-big-padding']").click() # нажимаем на кнопку Добавить

        time.sleep(25)

    def tear_down(self):
        time.sleep(25)
        self.driver.quit() # браузер закрывакем

if __name__ == "__main__":
    unittest.main()










