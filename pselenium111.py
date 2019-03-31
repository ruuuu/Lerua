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
from selenium.common.exceptions import NoSuchElementException

# #driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver.get("https://leroy-fabrica.herokuapp.com/ideas?creation=idea")
# #assert "Python" in driver.title
# elem = driver.find_element_by_name("q") # получение поля поиска по его атрибуту  name
# #elem.send_keys(Keys.ENTER)
#
# #elem.send_keys("Руфина") # вводим в поле поиска "Руфина"
# #elem.send_keys(Keys.RETURN)
# #assert "No results found." not in driver.page_source
# #driver.close() # закрывает браузер
# #driver.quit()# закрывает браузер
#
#
# elem = driver.find_element_by_class_name("lm-input lm-input-big ng-dirty ng-valid ng-touched")
# elem.send_keys("название идейки")
# driver.find_element_by_class_name()
# #class LoginMailBox(unittest.TestCase):
# #
# #    def setUp(self):
# #        #self.driver = webdriver.Firefox()
# #        self.driver = webdriver.Chrome()
# #        #self.driver.implicitly_wait(5)
# #
# #
# #    def test_user_login(self):
# #        driver = self.driver
# ##        driver.get("https://mail.ukr.net/desktop/login")
# ##        #login_field = driver.find_element_by_id("id-1") #поиск элемента по его id=id-1
# ##        login_field = driver.find_element_by_name("Login")
# ##        login_field.send_keys("autotestorgua") #ввод autotestorgua в элемент(в  нашем случае поле логина)
# ##        password_field = driver.find_element_by_id("id-2")#поиск элемента по его id=id-2
# ##        password_field.send_keys("testpass")#ввод testpass в элемент(в  нашем случае поле пароля)
# ##        button_login = driver.find_element_by_xpath("//*[text()='Увійти']")
# ##        button_login.click()#нажатие на элемент
# ##        #user_mail = driver.find_element_by_xpath("//*[@class='login-button__user']")
# ##        assert "No results found." not in driver.page_source
# ##        #assert user_mail.text == "autotestorgua@ukr.net"
# #
# #        # для леруа:
# #        driver.get("https://leroy-fabrica.herokuapp.com/main?popup=login")
# #        login_field = driver.find_element_by_name("login")
# #        login_field.send_keys("admin@mail.ru") #ввод "admin@mail.ru" в элемент(в  нашем случае поле логина)
# #        password_field = driver.find_element_by_name("password")
# #        password_field.send_keys("password")#ввод
# #        button_login = driver.find_element_by_xpath("//*[text()='ВОЙТИ']")
# ##       # driver.find_elements_by_class_name()
# ##        button_login.click()#нажатие на элемент
# #
# #        # login_field = driver.find_element_by_class_name("lm-input.ng-pristine.ng-invalid.ng-touched")
# #        # login_field.send_keys("admin@mail.ru")
# #        # password_field = driver.find_element_by_class_name("lm-input ng-pristine ng-invalid ng-touched")
# #        # password_field.send_keys("password")
# #        #
# #    def tear_down(self):
# #        self.driver.quit()
# #
# #if __name__ == "__main__":
# #    unittest.main()

from random import random, randrange, randint

# for i in range(0,15):
#     #print( randint(0, 4)) # выводит любое числов  диапзаоне от 0 до 4 включительно
#     print(i)


#print(randint([0, 7, 6, 5]))
# if False != False:
#     print("False == False")
# else:
#     print(" услвоие не истинно")
#
#
# if False is False:
#     print("False is False")

# class testclass(unittest.TestCase):
#
#     def authorization(self, driver):  # авторизация
#
#         driver.get('https://admin:LY1R1VMXJ1@dev.leroyfactory.ru')  # чтобы обойти базовую аунтентификацию
#         # driver.get("https://dev.leroyfactory.ru/main")

        # #кнопка Войти:
        # WebDriverWait(driver, 10).until(
        #     ec.presence_of_all_elements_located((By.XPATH,
        #                                          "//a[@class='link link-block']")))[6].click()
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





    #
    # def setUp(self):
    #
    #     self.driver = webdriver.Chrome()
    #     # self.driver = webdriver.Safari()
    #     self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
    #
    #     self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
    #
    # def test_method(self):
    #     driver = self.driver
    #     self.authorization(driver)  # вызываем метод, котрый выше
    #




# if voity.is_displayed():  # если кнпока видна ,  пусть даже будет задизейюдена  она, то
#     print(" кнопка видима")
# else:
#     print("кнопка евидима")
#
# if voity.is_enabled(): # если кнопка кликабельна
#     print(" кнопка незадизейблена, она кликабельна")
#
#
#
# else:
#     print("кнопка задиейблена")
#
# if voity.is_selected():
#     print("кнопка Войи выделеан")
# else:
#     print("кноку не выделена")

        # time.sleep(5)
        #
        # WebDriverWait(driver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, "//a[@href ='/sobytiya']"))).click()
        #
        # time.sleep(2)
        #
        # WebDriverWait(driver, 10).until(
        #             ec.presence_of_all_elements_located((By.XPATH, "//div[@class='events-card-wrapper']")))[0].click()
        #
        # time.sleep(2)
        #
        #
        # #
        # if elem.is_displayed():
        #      elem.click()
        #      print("элемент есть ")
        #
        # else:
        #     print("эдемента нет")
        #

        # try:
        #     elem = driver.find_element_by_xpath( # кнопка Перенести
        #         "//button[@class='btn lm-registration-action-btn lm-registration-action-btn-move']")
        #     time.sleep(5)
        #     elem.click()
        #     print("элемент Перенести найден, Записаться не найден")
        #
        # except NoSuchElementException: # если нет кнопки Перенести
        #
        #     elem2 = driver.find_element_by_xpath(  # кнопка Перенести
        #         "//button[@class='btn btn-green']")
        #
        #     time.sleep(5)
        #     elem2.click()
        #     print("эдемнет Записаться найден, еренести не найден")
        #

#
#         try:
#             elem = driver.find_element_by_xpath( # кнопка Отменить у события
#                 "//button[@class='btn lm-registration-action-btn lm-registration-action-btn-cancel']")
#             time.sleep(5)
#
#             elem.click()
#             print("элемент Отменить найден, Записаться не найден", elem.size)
#
#
#
#         except:
#
#             # если нет кнопки Отменить у сбытия
#
#             elem2 = driver.find_element_by_xpath(  # кнопка Записаться
#                 "//button[@class='btn btn-green event-body-btn-price']")
#
#             time.sleep(5)
#             elem2.click()
#             print("эдемнет Записаться найден, Отменить не найден", elem2.size)
#
#
#
#
#
#
#     def tear_down(self):
#         time.sleep(30)
#         self.driver.quit()
#
# if __name__ == "__main__":
#     unittest.main()
#
#


# try:
#
#     if 4%2==1:  # если в блоке try что-то неполучится сделвть, то пеерйдет нв блок except
#         print("число четное") # если словие в  if  не выполняется, то в блок except он не пойдет
#
# except:
#     print("число нечетное")
#

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



    def comment_k_mk(self, driver): # отсавляем коммент к рандомному  мк:

        time.sleep(2)

        list_cards = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='courses-card-wrapper']"))) # список всех крачоек мк

        rand_index = randint(0,len(list_cards)-1) # генерит индекс мк
        print("random index od cards mk equal", rand_index, ",count of cards mk equal", len(list_cards))

        driver.execute_script("arguments[0].scrollIntoView(true);",
                                  list_cards[rand_index])  # скриллим к этому элемементу list_cards[rand_index] ПОМОГЛО!!

        time.sleep(2)
        list_cards[rand_index].click()

        time.sleep(2)
        comment_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='comment-item btn write-comment-btn']")))

        time.sleep(2)
        # driver.execute_script("arguments[0].scrollIntoView(true);",
        #                       comment_button)  # скриллим к этому элемементу comment_buttonПОМОГЛО!!


        # Здесь он сам скроллит, пожтому не нужно скроллить  сам
        print("scroll to", comment_button.location['x'],comment_button.location['y'])
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

        print("count of buttons Otvetit+хxOtvet equal", len(otvetit_buttons))

        rand_index_button_otvetit = randint(0, len(otvetit_buttons) - 1)  # выбираем рандомный индекс кнопки Ответить или "ххОтвет"
        print("random index of button Otvetit/хxOtvet equal", rand_index_button_otvetit)

        if len(otvetit_buttons) == 1:
            otvetit_buttons[rand_index_button_otvetit].click()

        else:
            driver.execute_script("arguments[0].scrollIntoView(true);", otvetit_buttons[rand_index_button_otvetit])  # скриллим к этому элемементу ideas_cards[rand_index_for_idea] ПОМОГЛО!!
            time.sleep(2)
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
        events_page.click()

        events_cards = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='events-card-wrapper']"))) # спсиок картчоек событий

        rand_index_for_event = randint(0, len(events_cards)-1) # генерим индекс события
        print("random index od cards event equal", rand_index_for_event, ",count of cards event equal", len(events_cards))

        driver.execute_script("arguments[0].scrollIntoView(true);",
                              events_cards[rand_index_for_event])  # скриллим к этому элемементу events_cards[rand_index_for_event] ПОМОГЛО!!


        time.sleep(2)
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

        print("count of buttons Otvetit+хxOtvet equal", len(otvetit_buttons))

        rand_index_button_otvetit_or_хxOtvet = randint(0, len(otvetit_buttons) - 1)  # выбираем рандомный индекс кнопки Ответить или "ххОтвет"
        print("random index of button Otvetit/хxOtvet equal", rand_index_button_otvetit_or_хxOtvet)

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
        ideas_page.click()

        ideas_cards = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='lm-card-wrapper']"))) # список картчоек идей

        rand_index_for_idea = randint(0, len(ideas_cards)-1) # генерим  индекс идеи


        driver.execute_script("arguments[0].scrollIntoView(true);",
                                  ideas_cards[rand_index_for_idea])  # скриллим к этому элемементу ideas_cards[rand_index_for_idea] ПОМОГЛО!!



        time.sleep(2)
        ideas_cards[rand_index_for_idea].click()
        time.sleep(2)

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

        print("count of buttons Otvetit+хxOtvet equal", len(otvetit_buttons))

        rand_index_button_otvetit = randint(0, len(otvetit_buttons)-1) # выбираем рандомный индекс кнопки Ответить или "ххОтвет"
        print("random index of button Otvetit/хxOtvet equal", rand_index_button_otvetit)


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

        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        self.driver.set_window_position(0, 0) # устанавливает позицию левого вурзнего угла окна браузера

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()
        #self.driver.fullscreen_window() # откроет браузер на весь экзан





    def test_created_comments(self):

        driver = self.driver
        self.authorization(driver)  # вызво с регитсрации

        time.sleep(2)

        try:
            element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/master-klassy']"))) #код будет ждать 10 секунд до того, как отдаст исключение TimeoutException или если найдет элемент за эти 10 секунд, то вернет его.
            element.click()# кликаем по ссылке "Обучение"
        except TimeoutError:

            print("reference is not clickable")  #


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

