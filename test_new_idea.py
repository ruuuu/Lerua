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


    def setUp(self):

        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
            "browserName": "chrome",
        })
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

        # главное фото:
        WebDriverWait(driver, 18).until(ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(
            "/Users/rufina/Desktop/Леруа/Metal.jpg")

        #название идеи:
        elem = WebDriverWait(driver, 18).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname ='title']" ))) # идет заполняем название идеи
        elem.send_keys("idea")

        time.sleep(1)# краткое описание:
        elem1 = WebDriverWait(driver, 18).until(ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname ='description']" ))) # идет описание идеи
        elem1.send_keys("zapolnudfsd")

        time.sleep(2) #сложность:
        elem3 = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//label[@class='complexity-setter-item-label']")))[2] #  трудно

        elem3.click()

        time.sleep(2)
        # тогглер Нужны спец навыки:
        elem_toggler = WebDriverWait(driver, 18).until(ec.presence_of_element_located((By.XPATH, "//span[@class ='lm-toggle-slider']" )))
        elem_toggler.click()  #

        time.sleep(2)

        dictionary_for_ability = {1 : "navyk1", 2 : "navyk2", 3 : "navyk3", 4 : "navyk44"}
        for i in range(0, 4): #

                WebDriverWait(driver, 18).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Добавить навык']")))[i].send_keys(dictionary_for_ability[i+1])


        # add_skills_1 = driver.find_elements_by_xpath("//input[@placeholder='Добавить навык']")[0]  # добавить навык
        # add_skills_1.send_keys("навык1")
        #
        # add_skills_2 = driver.find_elements_by_xpath("//input[@placeholder='Добавить навык']")[1]  # добавить навык
        # add_skills_2.send_keys("навык2")
        #
        # add_skills_3 = driver.find_elements_by_xpath("//input[@placeholder='Добавить навык']")[2]  # добавить навык
        # add_skills_3.send_keys("навык3")


        time.sleep(2) # время выполнения:
        # переходим к элементу время выполнения, СКРОЛЛИМ
        actions = ActionChains(driver)  # создаем объект клааса ActionChains


        elem2 = driver.find_element_by_xpath("//input[@formcontrolname='duration']")  # у тега input есть атрибут duration со значением duration
        actions.move_to_element(elem2 ).perform()  # переходим в к элементу elem2
        time.sleep(2)
        elem2.send_keys("2")

        time.sleep(2)# Материалы:

        d_name_materials = {1: "material1", 2: "material2", 3: "material3"} # словарь для названия материалов
        d = {1: 150, 2: 189, 3: 450} # словарь для значений  полей стоимости

        for i in range(0, 3):

            add_matearil = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Добавить материал']")))[i].send_keys(d_name_materials[i+1])

            time.sleep(2)
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@type='number']")))[i+1].send_keys(d[i+1])

            time.sleep(2)
            driver.find_elements_by_xpath("//div[@class='where-find-item-content where-find-item-content-fabric']")[
                i].click()  # на фаьрике

            if i == 1:
                driver.find_elements_by_xpath("//div[@class='where-find-item-content where-find-item-content-leroy']")[
                    i].click()  # в магазине леруа






        # elem4 = WebDriverWait(driver, 10).until(
        #     ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Добавить материал']")))[0]
        # elem4.send_keys("материал1")
        #
        # WebDriverWait(driver, 10).until(
        #     ec.presence_of_all_elements_located((By.XPATH, "//input[@type='number']")))[1].send_keys("150")
        # time.sleep(1)
        # driver.find_elements_by_xpath("//div[@class='where-find-item-content where-find-item-content-fabric']")[0].click()  # на фаьрике
        #
        # time.sleep(2)# Материалы:
        #
        # WebDriverWait(driver, 10).until(
        #     ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Добавить материал']")))[1].send_keys("материал2")
        # time.sleep(1)
        # WebDriverWait(driver, 10).until(
        #     ec.presence_of_all_elements_located((By.XPATH, "//input[@type='number']")))[2].send_keys("180")
        # time.sleep(1)
        # driver.find_elements_by_xpath("//div[@class='where-find-item-content where-find-item-content-leroy']")[1].click()  # в леруа
        # time.sleep(1)
        # driver.find_elements_by_xpath("//div[@class='where-find-item-content where-find-item-content-fabric']")[1].click()  # на фаьрике




        time.sleep(2)# тип испольуземых материалов:
        check_box = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='material-types-item']")))[2]

        if check_box.is_displayed() is False: # если элемент невидимый
            print("element in not visible")
            actions.move_to_element(check_box).perform() # скриллим к этому элемементу



        time.sleep(2)
        check_box.click()  #
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='material-types-item']")))[4].click()

        time.sleep(2)

        # ИНТСРУМЕНТЫ:
        dictionary_equipment = {0: 1, 1: 3, 2: 4, 3: 2}
        for i in range(0, 4):

            search_elem_1 = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск по названию']")))
            driver.execute_script("arguments[0].scrollIntoView(true);",
                                  search_elem_1)  # скриллим к этому элемементу search_elem_1 ПОМОГЛО!!
            time.sleep(1)
            search_elem_1.click()
            time.sleep(1)
            WebDriverWait(driver, 20).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='search-results-item']")))[dictionary_equipment[i]].click() # выбрали обоудованеи из спсика

            time.sleep(2)



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

        d_name_step = {1: "step1", 2: "step2", 3: "step3", 4: "step4"}
        d_name_step_title = {1: "//input[@id='step-title-1']", 2: "//input[@id='step-title-2']", 3: "//input[@id='step-title-3']", 4: "//input[@id='step-title-4']"}
        d_name_description_step = {1: "description1", 2: "description2", 3: "description3", 4: "description4"}

        #  4 фото к  i- му шагу:
        file_dictionary = {1: "/Users/rufina/Desktop/Леруа/Metal.jpg", 2: "/Users/rufina/Desktop/Леруа/zima_01.jpg",
                           3: "/Users/rufina/Desktop/Леруа/zima13.jpg"}

        add_step = driver.find_element_by_xpath("//button[@class='btn btn-red-plus']") # красная кнопка Добавить шаг


        while i < 100: # скроллим к концу станицы
            scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
            i += 1

        for i in range(0, 4):

            if i != 0:
              while j < 100: # чтобы скроллиить к  концу станицы
                 scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
                 j += 1

            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, d_name_step_title[i+1]))).send_keys(d_name_step[i+1])  # номер шага

            time.sleep(2)
            WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//div[@data-placeholder='Введите инструкции']")))[i].send_keys(d_name_description_step[i+1])# опсиание шага

            time.sleep(2)
            for k in range(0, 3): # прикрепляем 4 фото к i-му шагу
                element_file = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[i+1].send_keys(
                    file_dictionary[k+1])
                time.sleep(1)

            if i == 3:
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
        #add_button = driver.find_element_by_xpath("//button[@class='btn btn-green btn-green-big-padding']")  # кнопка Добавить
        #add_button.click()

        time.sleep(25)

        #  Удалить без сохранения
        # remove_button = driver.find_element_by_xpath("/html/body/app-root/app-idea-creation/div/footer/div/div[2]/button") # так не  находит
        # remove_button.click()

    def tear_down(self):
        time.sleep(25)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()




# time.sleep(1)
# # загрузка файла перед шагами
# element_file2 = driver.find_element(by=By.XPATH, value="/html/body/app-root/app-idea-creation/div/form/div[1]/div[1]/section[7]/div[2]/app-file-picker/div/div/label/input")
# element_file2.send_keys("C:\\Users\\usse\\Desktop\\для теста_Леруа\\dog.jpg")
#
#
# time.sleep(2)
# elem_step = driver.find_element_by_xpath('//*[@id="step-title-1"]') # номер шага
# elem_step.send_keys("шаг 1")
# driver.find_element(by=By.XPATH, value="/html/body/app-root/app-idea-creation/div/section/div[1]/div[2]/div/app-idea-media-picker/div[1]/label/input").send_keys("C:\\Users\\usse\\Desktop\\для теста_Леруа\\dog.jpg")
# time.sleep(2)
# elem_step_area = driver.find_element_by_xpath('//*[@id="editor-1"]/div[1]') # опсиание шага
# elem_step_area.send_keys("полное описание шага1")
# #
#
# time.sleep(6)
# add_step_circle = driver.find_element_by_xpath("//button[@class='btn btn-red-plus']")# кнопка Добавить шаг
# add_step_circle.click()
#
# time.sleep(5)
# ##                                      //input[@id='step-title-2']
# elem_step = driver.find_element_by_xpath('//*[@id="step-title-2"]') # номер шага
# elem_step.send_keys("шаг 2")
# driver.find_element(by=By.XPATH, value="/html/body/app-root/app-idea-creation/div/section/div[2]/div[2]/div/app-idea-media-picker/div[1]/label/input").send_keys("C:\\Users\\usse\\Desktop\\для теста_Леруа\\dog.jpg")
#
#
# time.sleep(5)
# ##                                          //div[@class='ql-editor ql-blank']
# elem_step_area = driver.find_element_by_xpath('//*[@id="editor-2"]/div[1]') # опиcание шага
# elem_step_area.send_keys("полное описание шага2")
#
# # загрузка фото элемент ниже <input _ngcontent-c83="" ng2fileselect="" type="file">
# element_file1 = driver.find_element(by=By.XPATH, value="/html/body/app-root/app-idea-creation/div/form/div[2]/div/app-single-media-picker/label/input") # берем элемент input type='file'
# element_file1.send_keys("C:\\Users\\usse\\Desktop\\для теста_Леруа\\dog.jpg")
#
# time.sleep(6)
# add_button = driver.find_element_by_xpath("//button[@class='btn btn-green btn-green-big-padding']") # кнопка Добавить
# add_button.click()



#  Удалить без сохранения
#remove_button = driver.find_element_by_xpath("/html/body/app-root/app-idea-creation/div/footer/div/div[2]/button") # так не  находит
#remove_button.click()
