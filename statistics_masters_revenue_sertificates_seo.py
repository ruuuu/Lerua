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


class statistics_masters_seo_revenue_sertificates(unittest.TestCase):


    def authorization(self, driver): # авторизация

        driver.get('https://admin:LY1R1VMXJ1@dev.leroyfactory.ru') #  чтобы обойти базовую аунтентификацию
        #driver.get("https://dev.leroyfactory.ru/main")


        # кнопка Войти:
        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//a[@class='link link-block']" )))[6]
        button_voity.click()

        #  поле Логин
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='login']"))).send_keys("superadmin@mail.ru")

        #  поле ПАРОЛЬ
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys(
            "password")

        # кнопка Войти в форме авторизации
        voity = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn-green btn signin-submit-button']" )))



        if voity.is_displayed():  # если кнпока видна , то
            voity.click()



    def masters_statistic(self, driver):

        # нажимам на Подробнее в  стаистике мастеро
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/profile/superadmin/masters']"))).click()

        list_areas = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//label[@class='filter-item-wrapper']")))

        for i in range(0, len(list_areas)):
            list_areas[i].click()
            time.sleep(2)

        list_areas[0].click()  # жмем на Все
        time.sleep(2)

        active_elem = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn lm-sort-buttons-up lm-sort-buttons-active']")))

        # active = driver.find_element_by_xpath("//button[@class='btn lm-sort-buttons-up lm-sort-buttons-active']")

        # ситруме по возсрастаниюи  убываниюЖ
        arraws_up = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//button[@class='btn lm-sort-buttons-up']")))

        arraws_down = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//button[@class='btn lm-sort-buttons-down']")))
        print("колво верхних стрелок", len(arraws_up))

        print("колво верхних стрелок", len(arraws_down))

        # active_elem.cliсk() # кликаем первую верхнюю стрелку
        time.sleep(2)
        arraws_down[0].click()  # кликаем первую  нижнюю стрелку
        time.sleep(2)

        for i in range(0, len(arraws_up)):  # (0,4)

            # if active_elem.get_attribute("class") == "btn lm-sort-buttons-up lm-sort-buttons-active":
            #     active_elem.click()

            arraws_up[i].click()
            time.sleep(2)
            arraws_down[i + 1].click()

        time.sleep(2)

        for i in range(0, 5):  # жме мна пердыдущий месяц

            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='btn list-button list-button-prev']"))).click()
            time.sleep(2)

        for i in range(0, 5):  # жме мна следующий  месяц

            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='btn list-button list-button-next']"))).click()
            time.sleep(2)

        # жмем на сам месяц
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn viewport']"))).click()

        time.sleep(2)

        list_months = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='month-item']")))

        print("колво мсяцнв равно", len(list_months))

        # в попапе жмем кнопку передыдущего месяца
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn month-prev-btn month-btn-item']"))).click()

        time.sleep(2)

        for j in range(0, len(list_months)):
            list_months[j].click()
            time.sleep(2)

        #
        for i in range(0, 3):
            # в попапе жмем кнопку следующего  месяца
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='btn month-next-btn month-btn-item']"))).click()

            time.sleep(2)

            for j in range(0, len(list_months)):
                list_months[j].click()
                time.sleep(2)

        time.sleep(2)

        self.poisk_in_masters_statistics(driver)  # вызов метода котрый выше

        time.sleep(1)
        # кнопка Скачаьб [lsx
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn download-btn']"))).click()

        time.sleep(2)

        # кнопка Загрузить расписание
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn upload-btn lm-sm-none']"))).click()

        time.sleep(2)

        # кнопка крестик
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn lm-modal-close-btn']"))).click()

        time.sleep(2)

        # жмем кнопку Добавить
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn btn-add-idea add-btn']"))).click()

        time.sleep(3)
        # жмем крестик
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn lm-creation-header-close-btn']"))).click()

        # жмем кнопку зеделену вверху Назфд
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn btn-back']"))).click()



    def poisk_in_masters_statistics(self, driver):

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




    def poisk_in_statistic_sertificates(self, driver):

        time.sleep(2)
        # жмем иконку лупы
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn search-btn']"))).click()
        time.sleep(2)

        # жме мна крестик
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn close-btn']"))).click()
        time.sleep(2)

        # снова  жмем иконку лупы
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn search-btn']"))).click()
        time.sleep(2)

        result = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск...']")))
        time.sleep(1)
        result.send_keys("Александр")
        time.sleep(1)
        result.send_keys(Keys.ENTER)  # нажатие клавиши ентер
        time.sleep(3)

        # нажатие на кнпоку крестик
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn masters-search-query-remove']"))).click()



    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_other_statistics(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода  авторизации,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось

        # нажимаем на кионку профиля супералмина
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/profile']"))).click()
        time.sleep(6)

        # зеленая кнопка Администартор
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@class='link link-block btn btn-green-border']"))).click()

        time.sleep(4)

        #self.masters_statistic(driver) # вызов метода

        # жем на Подробнее у настроек SEO
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/profile/superadmin/seo-settings']"))).click()

        time.sleep(2)

        # нажимаем на кнопку Назад
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-back']"))).click()

        time.sleep(2)

        # статитсика по сертификатм:
        # нажимаем на Подробнее
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/profile/superadmin/certificates']"))).click()

        time.sleep(2)

        # нажимаем на кнпоку предыдущел месяца
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn list-button list-button-prev']"))).click()

        time.sleep(2)


        list_items = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//label[@class='filter-item-wrapper']")))

        for i in range(0, len(list_items)): # Все, Часы, Мастер-кдассы

            list_items[i].click()
            time.sleep(2)

        list_items[0].click()
        time.sleep(2)

        list_down_arraws = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn lm-sort-buttons-down']")))

        list_up_arraws = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn lm-sort-buttons-up']")))

        for i in range(0, len(list_down_arraws)):

            list_up_arraws[i].click()
            time.sleep(2)
            list_down_arraws[i].click()


        time.sleep(2)

        # жмем на сам месяц
        WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn viewport']"))).click()

        time.sleep(2)


        for i in range(0,3):
            #  в попапе жмем на предудущий месяц
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn month-prev-btn month-btn-item']"))).click()
            time.sleep(2)

        for i in range(0,2):
            #  в попапе жмем на следующий месяц
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn month-next-btn month-btn-item']"))).click()
            time.sleep(2)

        list_months = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='month-item']")))


        for i in range(0, len(list_months)):

            list_months[i].click()
            time.sleep(2)

        # кнопка Показать за все время
        WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH,  "//button[@class='btn months-footer']"))).click()


        time.sleep(2)

        self.poisk_in_statistic_sertificates(driver) # вызов меотда поиска

        time.sleep(2)
        # жмем кнопку Скачать xlsx
        WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn download-btn']"))).click()

        time.sleep(2)
        # жмем зедленую кнопку Назад верхнюю
        WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-back']"))).click()




    def tear_down(self):
        time.sleep(25)
        self.driver.quit() # закрываем браузер
        #self.driver.close() # выход из сессии браузер
        # pass


if __name__ == "__main__":
    unittest.main()



