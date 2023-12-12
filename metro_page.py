from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


MAIN_PAGE_URL = 'https://qa-metro.stand-1.praktikum-services.ru'

class Locators:
    MAIN_PAGE_SCHEME = [By.XPATH, ".//body//div[@data-block='scheme-view']"]
    FIELD_FROM = [By.XPATH, ".//body//div[@class='sidebar']//input[@placeholder='Откуда']"]
    FIELD_TO = [By.XPATH, ".//body//div[@class='sidebar']//input[@placeholder='Куда']"]

    # FIELD_FROM_DROP = [By.XPATH, "(.//body//div[@class='sidebar']//div[@data-block='y-suggest-drop'])[1]"]
    FIELD_FROM_LIST_ITEM = [By.XPATH, "(.//ul[@class='y-suggest-drop_islet__items'])[1]/li"]
    FIELD_TO_LIST_ITEM = [By.XPATH, "(.//ul[@class='y-suggest-drop_islet__items'])[2]/li"]
    # FIELD_FROM_LABEL = [By.XPATH, ".//span[@class='station-label__text']"]
    FIELD_FROM_LABEL = [By.XPATH, "(.//ul[@class='y-suggest-drop_islet__items'])[1]/li//span[@class='station-label__text']"]
    FIELD_TO_LABEL = [By.XPATH, "(.//ul[@class='y-suggest-drop_islet__items'])[2]/li//span[@class='station-label__text']"]


class MetroPage:

    def __init__(self, driver):        self.driver = driver

    # Общие методы для работы со страницами
    def open_main_page(self):
        """ Открываем страницу по URL {page_url} """
        self.driver.get(MAIN_PAGE_URL)

    def wait_for_load_element(self, locator):
        """ Ждем загрузку элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_for_present_element(self, locator):
        """ Ждем загрузку элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(locator))

    def wait_for_open_main_page(self):
        """ Ждем открытие страницы при переходе по ссылке: {self.page_url} """
        return self.wait_for_load_element(Locators.MAIN_PAGE_SCHEME)

    def set_value(self, locator, value):
        """ Вводим текст в поле по локатору: {locator} """
        self.driver.find_element(*locator).send_keys(value)

    def set_field_from(self, station):
        self.set_value(Locators.FIELD_FROM, station)
        self.wait_for_present_element(Locators.FIELD_FROM_LABEL)
        # self.wait_for_load_element(Locators.FIELD_FROM_LABEL)
        self.click_field(Locators.FIELD_FROM_LIST_ITEM)
        # self.wait_for_load_element(Locators.FIELD_FROM_LABEL)

    def set_field_to(self, station):
        self.set_value(Locators.FIELD_TO, station)

    def click_field(self, locator):
        field = self.wait_for_load_element(locator)
        field.click()

    def click_field_from(self):
        self.click_field(Locators.FIELD_FROM)

    def click_field_to(self):
        self.click_field(Locators.FIELD_TO)


