import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time
from selenium.webdriver.support.ui import WebDriverWait  # ожида
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec

# # #driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver.get('https://admin:LY1R1VMXJ1@dev.leroyfactory.ru')  # чтобы обойти базовую аунтентификацию
# # driver.get("https://dev.leroyfactory.ru/main")
#
# #кнопка Войти:
# WebDriverWait(driver, 10).until(
#             ec.presence_of_all_elements_located((By.XPATH,
#                                                  "//a[@class='link link-block']")))[6].click()
#
# time.sleep(2)
# # атворизуемся
# login = driver.find_element_by_xpath("//input[@formcontrolname='login']")
# login.send_keys("admin@mail.ru")
#
# time.sleep(2)
# password_d = driver.find_element_by_xpath("//input[@formcontrolname='password']")
# password_d.send_keys("password")
#
# time.sleep(2)
# but_send = driver.find_element_by_xpath("//button[@class ='btn-green btn signin-submit-button']")  # отправть
# but_send.click()
# time.sleep(5)
#
# try:
#     element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
#                                                                               "//a[@href='/master-klassy']")))  # код будет ждать 10 секунд до того, как отдаст исключение TimeoutException или если найдет элемент за эти 10 секунд, то вернет его.
#     element.click()  # кликаем по ссылке "Обучение"
# except TimeoutError:
#
#     print("время истекло")  #
#
# time.sleep(2)
#
# try:  # кнопка Добавить
#     add = WebDriverWait(driver, 15).until(
#         ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-add-idea']")))
#     if add.is_displayed():
#         add.click()
# except TimeoutError:
#     print("время истекло")
#
#
# # нажимаем на календарь:
# calendar = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//span[@class='date-picker-placeholder']")))
#
# driver.execute_script("arguments[0].scrollIntoView(true);", calendar)  # скриллим к этому элемементу calendar ПОМОГЛО!!
# calendar.click()
# time.sleep(3)
# try:
#                 # выбираем дату
#                 day = WebDriverWait(driver, 10).until(
#                     ec.presence_of_all_elements_located((By.XPATH, "//div[@class='date-item-wrapper']")))[35]
#
#                 time.sleep(1)
#
#                 if day.is_enabled():# если элемент незадизейблен то жмем
#                     day.click()
#
# except TimeoutError:
#                 print("время выбора даты истекло")
#
# driver.find_element_by_xpath("//span[@class='master-select-placeholder']").click()
#
#
# k = 0
#
# elems = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='master-select-item']"))) #список мастеров
#
# #elems1= driver.find_elements_by_xpath("//div[@class='master-select-item']")
#
# print("число матеров ранво", len(elems))
# for i in elems:
#     print( " мастер равен ", i)
#     time.sleep(2)
#
#
#
# # while elems[k].is_displayed(): # если элемент виден то считаем
# #     time.sleep(2)
# #
# #     print(k, "ый элемент видимый")
# #     k += 1
# #
# #
# # # kk = k+1 # индекс  itemа с котрого элемент не виден уже
# # #
# # # if elems[kk].is_displayed() == False:
# # #     driver.execute_script("arguments[0].scrollIntoView(true);", elems[kk])
# # #     kk += 1
# #
# #
# # # master_item = Select(driver.find_element_by_xpath("//span[@class='master-select-placeholder']")) Select работает только с тегом <select>
# # # master_item.select_by_index(4)
# # # time.sleep(7)
# #
# #
# #
# # print("колво  видимых элементво  в спсике ранво", k+1)
# #
#
#
#
#
# # #assert "Python" in driver.title
# # #elem = driver.find_element_by_name("q") # получение поля поиска по его атрибуту  name
# #
# # #elem.send_keys("Руфина") # вводим в поле поиска "Руфина"
# # #elem.send_keys(Keys.RETURN)
# # #assert "No results found." not in driver.page_source
# # #driver.close() # закрывает браузер
# # #driver.quit()# закрывает браузер
# #
# #
# # elem = driver.find_element_by_class_name("lm-input lm-input-big ng-dirty ng-valid ng-touched")
# # elem.send_keys("название идейки")
# #
# # #class LoginMailBox(unittest.TestCase):
# # #
# # #    def setUp(self):
# # #        #self.driver = webdriver.Firefox()
# # #        self.driver = webdriver.Chrome()
# # #        #self.driver.implicitly_wait(5)
# # #
# # #
# # #    def test_user_login(self):
# # #        driver = self.driver
# # ##        driver.get("https://mail.ukr.net/desktop/login")
# # ##        #login_field = driver.find_element_by_id("id-1") #поиск элемента по его id=id-1
# # ##        login_field = driver.find_element_by_name("Login")
# # ##        login_field.send_keys("autotestorgua") #ввод autotestorgua в элемент(в  нашем случае поле логина)
# # ##        password_field = driver.find_element_by_id("id-2")#поиск элемента по его id=id-2
# # ##        password_field.send_keys("testpass")#ввод testpass в элемент(в  нашем случае поле пароля)
# # ##        button_login = driver.find_element_by_xpath("//*[text()='Увійти']")
# # ##        button_login.click()#нажатие на элемент
# # ##        #user_mail = driver.find_element_by_xpath("//*[@class='login-button__user']")
# # ##        assert "No results found." not in driver.page_source
# # ##        #assert user_mail.text == "autotestorgua@ukr.net"
# # #
# # #        # для леруа:
# # #        driver.get("https://leroy-fabrica.herokuapp.com/main?popup=login")
# # #        login_field = driver.find_element_by_name("login")
# # #        login_field.send_keys("admin@mail.ru") #ввод "admin@mail.ru" в элемент(в  нашем случае поле логина)
# # #        password_field = driver.find_element_by_name("password")
# # #        password_field.send_keys("password")#ввод
# # #        button_login = driver.find_element_by_xpath("//*[text()='ВОЙТИ']")
# # ##       # driver.find_elements_by_class_name()
# # ##        button_login.click()#нажатие на элемент
# # #
# # #        # login_field = driver.find_element_by_class_name("lm-input.ng-pristine.ng-invalid.ng-touched")
# # #        # login_field.send_keys("admin@mail.ru")
# # #        # password_field = driver.find_element_by_class_name("lm-input ng-pristine ng-invalid ng-touched")
# # #        # password_field.send_keys("password")
# # #        #
# # #    def tear_down(self):
# # #        self.driver.quit()
# # #
# # #if __name__ == "__main__":
# # #    unittest.main()



from random import randint, random
import secrets
from secrets import choice
import string


# list_slov = []
# for i in range(0, 5):  # цикл по колчиву слов
#
#             list_bukv = [] # заполняем егов  к цикле
#             for j in range(4):  # цикл по буквам в слове , 4 буквы в слове
#                 # print("слоов равно")
#                 list_bukv.append(' '.join([choice(string.ascii_letters + string.digits)]))
#
#             # print("слово равно", list_bukv )
#
#             list_slov.append(''.join(list_bukv))
#         # print(list_slov)
#
# print(str(' '.join(list_slov)))




list_characters =  ['A', 'B', 'C', 'D', 'E', 'F', 'G' , 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', '#', '*', '(', ')', '"', ',', '/', ']', '[', '}', '{', '"', '?', '!', '§', '±', '<', '№']

# print("индекс ранодомного элемента равен ",randint(0, len(list_characters)))
# print("рандомный символ из списк аравен", list_characters[randint(0, len(list_characters))])
# print()

print("длина спика равна ", len(list_characters))

# list_slov = []
# for i in range(9): # цикл по словам
#
#     kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове
#     print(" ")
#     print("на ", i, "итерации колв букв в слове равно ", kolvo_bukv_v_slove)
#
#     for j in range(kolvo_bukv_v_slove): # образуем слово из  букв
#         #print("рандомный  идекс символа равен  ", randint(0, len(list_characters)), "сам  рандомный символ равен ", list_characters[randint(0, len(list_characters)-1)])
#         print()
#         print(''.join([list_characters[randint(0, len(list_characters)-1)]]), end='')
#
#         #list_bukv.append(''.join([list_characters[randint(0, len(list_characters))]])+'')
#     print(end='')


#------------------------------------
#  рабочий вариант без предложений:
def my_metho_randem_stroka(kolvo_bukv_v_slove, count_slov):


    list_slov = []
    #kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

    for i in range(count_slov): #цикл по колву слов, будет 5 слов  строке

        list_bukv = []
        for j in range(kolvo_bukv_v_slove): # цикл по бкувам в i-ом слове

            list_bukv.append(' '.join([list_characters[randint(0, len(list_characters)-1)]]))

        list_slov.append(''.join(list_bukv))
    for_email = {0: "@yandex.ru", 1: "@mail.ru", 2:"@gmail.com"}
    return str(' '.join(list_slov))+for_email[randint(0,2)]


print(my_metho_randem_stroka(5, 1))



#------------------------------




# # рабочий вариантс предложениями:
# def  my_metho_with_predlojenie(kolvo_bukv_v_slove, count_slov, count_predlojeniy):
#
#   list_predloj = []
#
#   for k in range(count_predlojeniy):# цикл по колву предло;ений
#     list_slov = []
#     #kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове
#
#     for i in range(count_slov): #цикл по колву слов, будет 5 слов  строке
#
#         list_bukv = []
#         for j in range(kolvo_bukv_v_slove): # цикл по бкувам в i-ом слове
#
#             list_bukv.append(' '.join([list_characters[randint(0, len(list_characters)-1)]]))
#
#         list_slov.append(''.join(list_bukv))
#
#     list_predloj.append(' '.join(list_slov)+'.')
#
#
#   return str(' '.join(list_predloj))
#
#
# for p in range(4):
#     print()
#     #print(p, " ое предложение арвно")
#     print(my_metho_with_predlojenie(randint(3, 10), randint(3,10), randint(2,5))  )
#     print()





















# # -*- coding: utf-8 -*-
# """
# Created on Sun May 20 11:46:56 2018
#
# @author: usse
# """
#
# import time
# from random import random, randrange, randint
# import unittest
# import selenium
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


# # созданеи события с регитсрауцией в начале
# class Create_event_with_wait(unittest.TestCase):
#
#
#     def authorization(self, driver):  # авторизация
#
#         # для FF чтобы обойти бозов аунтентификацию
#         # aunthentification_token = str("Basic " + base64.b64encode(b'admin:LY1R1VMXJ1'))
#         #
#         # capa = DesiredCapabilities.PHANTOMJS
#         # capa['phantomjs.page.customHeaders.Authorization'] = aunthentification_token
#         # driver = webdriver.PhantomJS(desired_capabilities=capa)
#
#         driver.get('https://admin:LY1R1VMXJ1@dev.leroyfactory.ru')  # чтобы обойти базовую аунтентификацию
#         #driver.get("https://dev.leroyfactory.ru/main")
#
#         #кнопка Войти:
#         WebDriverWait(driver, 10).until(
#             ec.presence_of_all_elements_located((By.XPATH,
#                                                  "//a[@class='link link-block']")))[6].click()
#
#         time.sleep(2)
#         # атворизуемся
#         login = driver.find_element_by_xpath("//input[@formcontrolname='login']")
#         login.send_keys("admin@mail.ru")
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
#     def setUp(self):
#
#         self.driver = webdriver.Chrome()    #Firefox()
#         self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
#         self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
#
#         #self.driver.maximize_window()
#         # self.driver.implicitly_wait(10) # для  явных ожиданий, чтобы подгруздимь элементы
#
#
#
#     def test_create_event(self):
#
#         driver = self.driver
#         self.authorization(driver)  # вызываем метод, котрый выше
#         time.sleep(3)
#         #
#         try:# кликаем по ссылуе "Событие"
#             element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/sobytiya']"))) #код будет ждать 10 секунд до того, как отдаст исключение TimeoutException или если найдет элемент за эти 10 секунд, то вернет его.
#             element.click()
#         except TimeoutError: # TimeoutException
#             pass  # ничегон е будет делать
#
#
#         time.sleep(3)# чтобы посомртеть что происходит
#
#         try: # кнопа Добавить:
#             add = WebDriverWait(driver, 18).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-add-idea']")))
#             add.click()
#         except TimeoutError:
#             pass
#
#         time.sleep(2)
#
#         # главное фото прикрепляем:
#         file_dicitionary = {0: "/Users/rufina/Desktop/леруа/Metal.jpg", 1: "/Users/rufina/Desktop/леруа/orig.jpeg",
#                             2: "/Users/rufina/Desktop/леруа/s1200.jpeg", 3: "/Users/rufina/Desktop/леруа/zima13.jpg",
#                             4: "/Users/rufina/Desktop/леруа/12326gnHcPlbTVLECrewQp.jpg", 5: "/Users/rufina/Desktop/леруа/cavbczeweaahcaa-big.jpg",
#                             6: "/Users/rufina/Desktop/леруа/1371106736_67.jpg"}
#
#         WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[
#             0].send_keys(file_dicitionary[randint(0, len(file_dicitionary) - 1)]) # вставляет рандомную картинку из словаря
#
#             #send_keys("/Users/rufina/Desktop/Леруа/Metal.jpg")  #
#
#
#         name_event = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#             (By.XPATH, "//input[@formcontrolname='title']")))
#         name_event.send_keys("самое длинное событие")
#
#         #  ОРГАНИЗАТОРЫ радиокнпока (на ФАБРИКЕ  тоит по умолчанию)
#         time.sleep(2)
#
#         # жмем на радиокнопку:
#         WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
#                 (By.XPATH, "//div[@class='lm-radio-indicator']")))[1].click()
#         time.sleep(2)
#
#
#
#         #лого:
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,
#                                                                         "/html/body/app-root/app-event-creation/div/form/div/div[1]/div/section[2]/div[4]/div/div[1]/div[1]/app-logo-picker/label/input"))).send_keys(
#                 "/Users/rufina/Desktop/Леруа/idea_1920.jpg")  #
#
#
#         WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#                     (By.XPATH, "//input[@placeholder='Название']"))).send_keys("название организаторов0")
#
#         WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#                     (By.XPATH, "//input[@placeholder='https://']"))).send_keys("https://automated-testing.info/t/kak-opredelit-klikabelnost-elementa-na-stranicze-s-pomoshhyu-webdriver/3719/18")
#
#         doctinary_foto_f = {1: "/Users/rufina/Desktop/Леруа/zima13.jpg", 2: "/Users/rufina/Desktop/Леруа/zima_01.jpg"}
#
#         dicitionary_name_organizations = {1:"название организаторов1", 2: "название организаторов2"}
#
#         dicitionary_url = {1: "https://vk.com", 2: "https://facebook.com"}
#
#         dicitionary_xpath = {1: "/html/body/app-root/app-event-creation/div/form/div/div[1]/div/section[2]/div[4]/div/div[2]/div[1]/app-logo-picker/label/input",
#                            2: "/html/body/app-root/app-event-creation/div/form/div/div[1]/div/section[2]/div[4]/div/div[3]/div[1]/app-logo-picker/label/input"
#                            }
#
#         for i in range(1, 3):
#             # зеленая кнопка Добавить
#             WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#                 (By.XPATH, "//button[@class='btn btn-green-plus']"))).click()
#             # лого:
#             WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, dicitionary_xpath[i]))).send_keys(doctinary_foto_f[i])
#
#             WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
#                              (By.XPATH, "//input[@placeholder='Название']")))[i].send_keys(dicitionary_name_organizations[i])
#
#             WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
#                     (By.XPATH, "//input[@placeholder='https://']")))[i].send_keys(dicitionary_url[i])
#             time.sleep(2)
#
#
#
#         time.sleep(2)
#
#
#
#
#
#
#         # краткое описание:
#         WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#             (By.XPATH, "//input[@formcontrolname='shortDescription']"))).send_keys("cj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbt")
#
#         time.sleep(2)
#
#         #  Основное опсиание:
#         WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#             (By.XPATH,
#              "//textarea[@formcontrolname='mainDescription']"))).send_keys(
#             "основное опсианиеосновное опсианиеосновное опсианиеосновное опсианиеосновное опсианиеосновное опсианиеосновное опсианиеосновное опсианиеосновное опсианиеосновное опсианиеосновное опсианиеосновное опсианиеосновное опсианиеосновное опсиание ")
#
#         time.sleep(2)
#         # программа:
#         WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#             (By.XPATH,
#              "//textarea[@formcontrolname='program']"))).send_keys("ПограммаПограммаПограммаПограммаПограммаПограммаПограммаПограммаПограммаПограммаПограммаПограммаПограммаПограммаПограммаПограмма")
#
#         time.sleep(2)
#
#         # ссылка на программу:
#         WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#             (By.XPATH,
#              "//input[@formcontrolname='eventPageUrl']"))).send_keys("https://fkjgkdfg.com")
#
#         time.sleep(4)
#
#
#
#         # нажатие на календарь(для даты начвла):
#         calendar = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
#                 (By.XPATH, "//span[@class='date-picker-placeholder']")))[0]
#
#
#         driver.execute_script("arguments[0].scrollIntoView(true);", calendar) # скриллим к этому элемементу calendar ПОМОГЛО!!
#         time.sleep(2)
#         calendar.click()
#
#
#         time.sleep(5)
#         day_1_1 =  WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
#                 (By.XPATH, "//div[@class='date-item-content date-item-content-type-']")))
#
#         list_day_1 = [] # здесь будем хранить индексы активныx(не задзейбленные) первыx  дат
#         count_days_1 = 0 # число незадизейбелнных дат первогок аленаря
#
#         for i in range(0, len(day_1_1)): # выбираем первую незадизейбленную дату
#
#             if day_1_1[i].is_enabled() and day_1_1[i].is_displayed():  # если дата незадизейблина
#
#                 list_day_1.append(i)
#                 count_days_1 += 1
#
#         time.sleep(2)
#         print("число незадизейбленных дат первого каленаря", count_days_1)
#
#         # выбираем рандомный индекс из спсика активных дат:
#         k1 = randint(0, count_days_1-1)
#         print("рандомные индекс из спсика активных дат", k1)
#         day_1_1[list_day_1[k1]].click()
#
#         time.sleep(2)
#
#
#         # нажатие на календарь(для даты конца):
#
#         WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
#             (By.XPATH, "//span[@class='date-picker-placeholder']")))[0].click()
#
#         time.sleep(2)
#
#         day_1_2 = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
#             (By.XPATH, "//div[@class='date-item-content date-item-content-type-']")))
#
#         list_day_2 = []  # здесь будем хранить индексы активныx(не задзейбленные) вторых  дат
#
#         count_days_2 = 0  # число незадизейбелнных дат второго каленаря
#
#         # выбираем день:
#         for i in range(20+list_day_1[k1], len(day_1_2)):  # выбираем  незадизейбленную дату
#
#             if day_1_2[i].is_enabled() and day_1_2[i].is_displayed():  # если дата незадизейблина
#
#                 list_day_2.append(i)
#                 count_days_2 += 1
#
#         time.sleep(2)
#         print("число незадизейбленных дат второго каленаря", count_days_2 )
#
#         # выбираем рандомный индекс из спсика активных дат:
#         k2 = randint(0, count_days_2-1) # ДОДУМАТЬ!!!!!!
#         print("рандомный индекс из спсика активных дат", k2)
#         day_1_2[list_day_2[k2]].click()
#
#         time.sleep(2)
#
#
#
#
#
#         # выбираем время:
#         WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#             (By.XPATH,
#              "//input[@formcontrolname='time']"))).send_keys("10:00-11:00")
#
#         time.sleep(4)
#
#         # место проведения:
#
#         WebDriverWait(driver, 10).until(
#             ec.presence_of_all_elements_located((By.XPATH, "//div[@class='lm-radio-indicator']")))[3].click()
#
#         WebDriverWait(driver, 10).until(
#             ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='placeAddress']"))).send_keys("какое-то другое место проведения")
#
#
#         # радиокнопка  Стоимость:
#         WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#             (By.XPATH,
#              "//input[@formcontrolname='price']"))).send_keys("800")
#
#         time.sleep(2)
#
#         # указываем колво человек:
#         WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#             (By.XPATH,
#              "//input[@formcontrolname='maxCapacity']"))).send_keys("10")
#
#         time.sleep(2)
#
#         # указываем ссылку на регитсрацию:
#         WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#             (By.XPATH, "//input[@formcontrolname='registrationUrl']"))).send_keys("https://kgjhlkfjhlfjg.com") #
#
#         time.sleep(2)
#
#         # возрастное ограничение:
#         WebDriverWait(driver, 10).until(
#             ec.presence_of_all_elements_located((By.XPATH, "//label[@class='radio-group-wrapper']")))[3].click()
#
#         time.sleep(2)
#
#         # прикрепляем фото (4 штуки)
#         dictoinary_fotos = {1: "/Users/rufina/Desktop/Леруа/zima_01.jpg", 2: "/Users/rufina/Desktop/Леруа/orig.jpeg", 3: "/Users/rufina/Desktop/Леруа/kartinka-snegir.jpg", 4: "/Users/rufina/Desktop/Леруа/zima13.jpg"}
#
#         # for i in range(1, 5):
#         #
#         #     time.sleep(2) #
#         #WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[i].send_keys(dictoinary_fotos[i-1])  #
#
#         WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#             (By.XPATH, "/html/body/app-root/app-event-creation/div/form/div/div[3]/div/section[2]/div[2]/div/div[1]/div/div/app-single-media-picker/label/input"))).send_keys("/Users/rufina/Desktop/Леруа/images.jpeg")  #
#         time.sleep(2)
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-event-creation/div/form/div/div[3]/div/section[2]/div[2]/div/div[2]/div/div/app-single-media-picker/label/input"))).send_keys("/Users/rufina/Desktop/Леруа/zima13.jpg")  #
#         time.sleep(2)
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-event-creation/div/form/div/div[3]/div/section[2]/div[2]/div/div[3]/div/div/app-single-media-picker/label/input"))).send_keys("/Users/rufina/Desktop/Леруа/i.jpeg")  #
#         time.sleep(2)
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-event-creation/div/form/div/div[3]/div/section[2]/div[2]/div/div[4]/div/div/app-single-media-picker/label/input"))).send_keys("/Users/rufina/Desktop/Леруа/idea_1920.jpg")  #
#
#
#
#         # ссылка на фотоаьюбом
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname = 'albumUrl']"))).send_keys("https://vk.com/public42564857") #
#
#         time.sleep(2)
#
#         # Адрес
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname = 'address']"))).send_keys("Москва") #
#
#         time.sleep(2)
#
#         # Телефон
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname = 'phone']"))).send_keys("89807654387") #
#
#         time.sleep(2)
#
#         # Email
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname = 'email']"))).send_keys("ituroiu@ya.ru") #
#         time.sleep(5)
#
#
#
#         # element_file1 = driver.find_element(by=By.XPATH, value="")  # берем элемент input type='file'
#         # element_file1.send_keys("C:\\Users\\usse\\Desktop\\для теста_Леруа\\dog.jpg")
#         # time.sleep(6)
#
#
#
#
#         time.sleep(2)
#
#         # мессенждеры:
#         #fb:
#         add_messanger = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-green-plus btn-green-plus-trigger']")))
#
#         driver.execute_script("arguments[0].scrollIntoView(true);", add_messanger) #скролим к кнопке  add_messanger
#         time.sleep(2)
#         add_messanger.click()
#
#         time.sleep(1)
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located(
#                     (By.XPATH, "//button[@class='btn social-types-item lm-social-facebook']"))).click()
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located(
#             (By.XPATH, "//input[@placeholder='https://facebook.com/...']"))).send_keys("https://www.facebook.com/pages/category/Community/%D0%9A%D1%80%D0%B0%D1%81%D0%B8%D0%B2%D1%8B%D0%B5-%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-344648422268527/")
#
#         time.sleep(2)
#         #watsup:
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located(
#             (By.XPATH, "//button[@class='btn btn-green-plus btn-green-plus-trigger']"))).click()
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located(
#             (By.XPATH, "//button[@class='btn social-types-item lm-social-whatsapp']"))).click()
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located(
#             (By.XPATH, "//input[@placeholder='+7 (000) 123 45 67']"))).send_keys("89765437865")
#
#         time.sleep(2)
#         #twitter:
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located(
#             (By.XPATH, "//button[@class='btn btn-green-plus btn-green-plus-trigger']"))).click()
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located(
#             (By.XPATH, "//button[@class='btn social-types-item lm-social-twitter']"))).click()
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located(
#             (By.XPATH, "//input[@placeholder='https://twitter.com/...']"))).send_keys("https://twitter.com/alexey_pushkov")
#
#         time.sleep(2)
#
#
#         # сделать баннер:
#         # переключаем тогглер:
#         toggler = WebDriverWait(driver, 10).until(
#             ec.presence_of_all_elements_located((By.XPATH, "//span[@class='lm-toggle-slider']")))[1]
#
#         driver.execute_script("arguments[0].scrollIntoView(true);", toggler)  # скролим к элементу  toggler
#         time.sleep(1)
#         toggler.click()
#
#         time.sleep(1)
#         WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-event-creation/div/form/div/div[3]/div/section[5]/div[3]/div/app-single-media-picker/label/input"))).send_keys("/Users/rufina/Desktop/Леруа/idea_1920.jpg")
#
#         driver.find_element_by_xpath("//button[@class='btn btn-green btn-green-big-padding']").click() # нажимаем на кнопку Добавить
#
#         time.sleep(25)
#
#     def tear_down(self):
#         time.sleep(25)
#         self.driver.quit() # браузер закрывакем
#
# if __name__ == "__main__":
#     unittest.main()
#
#
#
#
#
#
#
#
