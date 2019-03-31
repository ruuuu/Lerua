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


class zakaz_abonementa(unittest.TestCase):


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
        self.driver = webdriver.Chrome() #webdriver.Chrome()
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_zakaz_abonementa(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода  авторизации,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось

        # переход к разделу Абонементы и услуги:
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/abonementy-i-uslugi']"))).click()
        time.sleep(5)

        zakaz_button = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='reserve-btn to-order']")))[0]

        driver.execute_script("window.scrollBy(834, 19);") # скроллим к этому месту

        #закакз абонемента часового
        for i in range(0, 5): # нажимаем на кнопку плюс
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//button[@class='calc-btn calc-plus btn']")))[0].click()
            time.sleep(1)

        for i in range(0, 2):
            WebDriverWait(driver, 10).until( # нажимаем на кнопку минус
                ec.presence_of_all_elements_located((By.XPATH, "//button[@class='calc-btn calc-minus btn']")))[0].click()
            time.sleep(2)

        zakaz_button.click() # жмем Заказкть

        time.sleep(2)

        # кнпока Назад
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn payment-back-btn']"))).click()
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='reserve-btn to-order']")))[
            0].click()  # жмем Заказкть
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='payment-card-icon-wrapper']"))).click()

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-link-back ']"))).click() # Вернуться на сайт


        # закакз абонемента дневного
        for i in range(0, 5):  # нажимаем на кнопку плюс
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//button[@class='calc-btn calc-plus btn']")))[1].click()
            time.sleep(1)

        for i in range(0, 2):
            WebDriverWait(driver, 10).until(  # нажимаем на кнопку vbyec
                ec.presence_of_all_elements_located((By.XPATH, "//button[@class='calc-btn calc-minus btn']")))[
                1].click()
            time.sleep(2)

        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='reserve-btn to-order']")))[
            1].click()  # жмем Заказкть

        time.sleep(2)
        # кнпока Назад
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn payment-back-btn']"))).click()

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='reserve-btn to-order']")))[
            1].click()  # жмем Заказкть
        time.sleep(2)

        time.sleep(2)
        # жмем на карту При обретси на месте
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='payment-card-icon-wrapper']"))).click()
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn btn-link-back ']"))).click()  # Вернуться на сайт











    def tear_down(self):
        time.sleep(25)
        #self.driver.quit()
        self.driver.close() # закрываем браузер
        # pass


if __name__ == "__main__":
    unittest.main()



