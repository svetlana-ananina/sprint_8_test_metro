from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


MAIN_PAGE_URL = 'https://qa-metro.stand-1.praktikum-services.ru'

class Locators:
    # MAIN_PAGE_SCHEME = [By.XPATH, ".//body//div[@data-block='scheme-view']"]
    MAIN_PAGE_MAP = [By.XPATH, ".//body//ymaps[@class='ymaps-2-1-79-inner-panes']"]
    # Поля ввода на боковой панели
    FIELD_FROM = [By.XPATH, ".//body//div[@class='sidebar']//input[@placeholder='Откуда']"]
    FIELD_TO = [By.XPATH, ".//body//div[@class='sidebar']//input[@placeholder='Куда']"]
    # Выпадающие списки при выборе станции
    FIELD_FROM_LIST_ITEM = [By.XPATH, "(.//ul[@class='y-suggest-drop_islet__items'])[1]/li"]
    FIELD_TO_LIST_ITEM = [By.XPATH, "(.//ul[@class='y-suggest-drop_islet__items'])[2]/li"]

    # Раздел выпадающего списка с выбором станции
    FIELD_FROM_LIST = [By.XPATH, "(.//div[@class='y-suggest-drop_islet__content _live-events'])[1]"]
    FIELD_TO_LIST = [By.XPATH, "(.//div[@class='y-suggest-drop_islet__content _live-events'])[2]"]
    # Элемент списка с названием станции
    FIELD_FROM_LIST_LABEL = [By.XPATH, "(.//div[@class='y-suggest-drop_islet__content _live-events'])[1]//li[@data-block='station-suggest-drop-item']"]
    FIELD_TO_LIST_LABEL = [By.XPATH, "(.//div[@class='y-suggest-drop_islet__content _live-events'])[2]//li[@data-block='station-suggest-drop-item']"]

    # иконки слева от выбранной станции
    FIELD_FROM_ICON = [By.XPATH, ".//div[@class='from-to-suggest__from-field']//span[@data-name='station-icon']"]
    FIELD_TO_ICON = [By.XPATH, ".//div[@class='from-to-suggest__to-field']//span[@data-name='station-icon']"]

    # FIELD_FROM_LABEL = [By.XPATH, ".//span[@class='station-label__text']"]

    # FIELD_FROM_LABEL = [By.XPATH, "(.//ul[@class='y-suggest-drop_islet__items'])[1]/li//span[@class='station-label__text']"]
    # FIELD_TO_LABEL = [By.XPATH, "(.//ul[@class='y-suggest-drop_islet__items'])[2]/li//span[@class='station-label__text']"]



class MetroPage:

    def __init__(self, driver):        self.driver = driver

    # Общие методы для работы со страницами
    def open_main_page(self):
        """ Открываем страницу по URL {page_url} """
        self.driver.get(MAIN_PAGE_URL)

    def wait_for_load_element(self, locator):
        """ Ждем загрузку элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_for_present_element(self, locator):
        """ Ждем загрузку элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator))

    def wait_for_open_main_page(self):
        """ Ждем открытие страницы при переходе по ссылке: {self.page_url} """
        return self.wait_for_load_element(Locators.MAIN_PAGE_MAP)
        #  return self.wait_for_present_element(Locators.MAIN_PAGE_MAP)

    def set_value(self, locator, value):
        """ Вводим текст в поле по локатору: {locator} """
        self.driver.find_element(*locator).send_keys(value)

    def click_field(self, locator):
        field = self.wait_for_load_element(locator)
        field.click()

    # вводим станцию в поле "Откуда"
    def select_from_station(self, station):
        self.set_value(Locators.FIELD_FROM, station)
        self.wait_for_load_element(Locators.FIELD_FROM_LIST_LABEL)
        self.click_field(Locators.FIELD_FROM_LIST_LABEL)
        self.wait_for_present_element(Locators.FIELD_FROM_ICON)

    # вводим станцию в поле "Куда"
    def select_to_station(self, station):
        self.set_value(Locators.FIELD_TO, station)
        #self.wait_for_present_element(Locators.FIELD_TO_LIST_ITEM)
        self.click_field(Locators.FIELD_TO_LIST_ITEM)
        self.wait_for_present_element(Locators.FIELD_TO_ICON)



