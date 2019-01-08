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

# созданеи события с регитсрауцией в начале
class Create_event_with_wait(unittest.TestCase):


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



    def setUp(self):

        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
            "browserName": "chrome",
        })
        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, чтобы подгруздимь элементы



    def test_create_event(self):

        driver = self.driver
        self.authorization(driver)  # вызываем метод, котрый выше
        time.sleep(3)
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
        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[
            0].send_keys("/Users/rufina/Desktop/Леруа/Metal.jpg")  #


        name_event = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='title']")))
        name_event.send_keys("name event")

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
                    (By.XPATH, "//input[@placeholder='Название']"))).send_keys("name_organixations0")

        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                    (By.XPATH, "//input[@placeholder='https://']"))).send_keys("https://automated-testing.info/t/kak-opredelit-klikabelnost-elementa-na-stranicze-s-pomoshhyu-webdriver/3719/18")

        doctinary_foto_f = {1: "/Users/rufina/Desktop/Леруа/zima13.jpg", 2: "/Users/rufina/Desktop/Леруа/zima_01.jpg"}

        dicitionary_name_organizations = {1:"name organizations1", 2: "name organizations2"}

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
            (By.XPATH, "//input[@formcontrolname='shortDescription']"))).send_keys("cj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbtcj,snbt_cj,snbt")

        time.sleep(2)

        #  Основное опсиание:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,
             "//textarea[@formcontrolname='mainDescription']"))).send_keys(
            "ldfmglfh sfhksflhk shss")
        time.sleep(2)
        # программа:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,
             "//textarea[@formcontrolname='program']"))).send_keys("ptogram ptogram ptogram")
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

        day_1 = WebDriverWait(driver, 10).until(
               ec.presence_of_all_elements_located((By.XPATH, "//div[@class='date-item-wrapper']")))[35]
        day_1.click()

        time.sleep(4)

        j = 0
        # #выбираем дату начала:
        # for i in range(0, 42):
        #
        #     if i == 13: # выбираем номер активной даты
        #         day_1 = WebDriverWait(driver, 10).until(
        #             ec.presence_of_all_elements_located((By.XPATH, "//div[@class='date-item-wrapper']")))[i]
        #         day_1.click()
        #         j = i
        #         break

            #day11 = driver.find_elements_by_xpath("//div[@class='date-item-wrapper']")[i]

            # if day_1.is_enabled(): # если элемент видимый, то кликаем
            #     day_1.click()
            #     break# как только нашоли первую активную кнопку так выходитм


        # нажатие на календарь(для даты конца):
        time.sleep(2)
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//span[@class='date-picker-placeholder']")))[0].click()

        time.sleep(2)
        day_2 = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//div[@class='date-item-wrapper']")))[80]
        day_2.click()

        # time.sleep(2)  # ждем пока подгрузится календарь

        # # выбираем дату конца:
        #for i in range(42, 84):

        # time.sleep(4)
        # day_2 = WebDriverWait(driver, 10).until(
        #         ec.presence_of_all_elements_located((By.XPATH, "//div[@class='date-item-wrapper']")))[j+43]
        # #time.sleep(2)
        # day_2.click()

        time.sleep(2)

        # выбираем время:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,
             "//input[@formcontrolname='time']"))).send_keys("10:00-11:00")

        time.sleep(4)

        # место проведения:

        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='lm-radio-indicator']")))[3].click()

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='placeAddress']"))).send_keys("fjgjd fdlhfdhk fhlfshfd dfhkfdh")


        # радиокнопка  Стоимость:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,
             "//input[@formcontrolname='price']"))).send_keys("800")

        time.sleep(2)

        # указываем колво человек:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,
             "//input[@formcontrolname='maxCapacity']"))).send_keys("10")

        time.sleep(2)

        # указываем ссылку на регитсрацию:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='registrationUrl']"))).send_keys("https://kgjhlkfjhlfjg.com") #

        time.sleep(2)

        # возрастное ограничение:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//label[@class='radio-group-wrapper']")))[3].click()

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
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname = 'address']"))).send_keys("Moscow") #

        time.sleep(2)

        # Телефон
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname = 'phone']"))).send_keys("89807654387") #

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
        WebDriverWait(driver, 20).until(ec.presence_of_element_located(
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

        # driver.find_element_by_xpath("//button[@class='btn btn-green btn-green-big-padding']").click() # нажимаем на кнопку Добавить

        time.sleep(25)

    def tear_down(self):
        time.sleep(25)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()








# driver.find_element_by_xpath("//input[@formcontrolname='title']").send_keys("событие 14-го июня")# вводим  с поле название события
        #
        # driver.find_elements_by_xpath("//div[@class='lm-radio-indicator']")[0].click()#  радиокнопки выбор на фабрике  или другой огранизатор
        #
        # driver.find_element_by_xpath("//input[@formcontrolname='shortDescription']").send_keys("короткое описание события")  # краткое описание
        #
        # driver.find_element_by_xpath("//textarea[@formcontrolname='mainDescription']").send_keys("полное описание события") # олное опсиание
        #
        # time.sleep(9)
        # driver.find_elements_by_xpath("//span[@class='date-picker-placeholder']")[0].click()# выбираем начальную дату события
        # time.sleep(8)# ждем пока  загрузится календарь
        # driver.find_elements_by_xpath("//div[@class='date-item']")[17].click()  #выбираем 5 июня
        #
        # time.sleep(5)
        # driver.find_elements_by_xpath("//span[@class='date-picker-placeholder']")[1].click()  # выбираем конечную дату события
        # time.sleep(8)  # ждем пока  загрузится календарь
        # driver.find_elements_by_xpath("//div[@class='date-item']")[60].click()  # выбираем
        #
        # time.sleep(5)
        # driver.find_element_by_xpath("//input[@formcontrolname='time']").send_keys("14:00-16:00") # вводим время события
        #
        # driver.find_elements_by_xpath("//div[@class='lm-radio-indicator']")[3].click()  # радиокнопки выбор на "В другом месте"
        # time.sleep(4)  # ждем пока  загурузится поле
        # driver.find_element_by_xpath("//input[@formcontrolname='placeAddress']").send_keys("Москва рлбротьбпа")  # вводим адрес
        #
        # time.sleep(7)
        # driver.find_elements_by_xpath("//div[@class='lm-radio-indicator']")[5].click()  # радиокнопки Стоимость
        # time.sleep(4)  # ждем пока  загурузится поле для стоимости
        # driver.find_element_by_xpath("//input[@formcontrolname='price']").send_keys("124") # указываес стоимость
        #
        # time.sleep(4)
        # driver.find_element_by_xpath("//span[@class='lm-toggle-slider']").click() # выключаем тоггглер
        #
        # # добавить регитсрацию на событе(тогглер)
        # time.sleep(6)  # ждем пока  загурузится
        # driver.find_elements_by_xpath("//label[@class='radio-group-wrapper']")[2].click() # кликаем возраст 12+
        #
        # # добавить  загузку 4 ех фоток фотки
        # time.sleep(6)
        # driver.find_element_by_xpath("//input[@formcontrolname='address']").send_keys("Калининград") # заполняем поле адрес
        #
        # driver.find_element_by_xpath("//input[@formcontrolname='phone']").send_keys("89378866789")  # заполняем поле телефон
        #
        # driver.find_element_by_xpath("//input[@formcontrolname='email']").send_keys("jfghjghd@mail.ru")  # заполняем поле
        #
        # # загрузка фото элемент ниже <input _ngcontent-c83="" ng2fileselect="" type="file">
        # time.sleep(6)


