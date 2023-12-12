import time

from selenium import webdriver

from metro_page import MetroPage


class TestMetroRoute:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_travel_time(self):
        main_page = MetroPage(self.driver)

        # Открываем Главную страницу
        main_page.open_main_page()

        # time.sleep(5)

        # Ждем загрузку схемы
        main_page.wait_for_open_main_page()

        main_page.select_from_station('Красные Ворота')

        time.sleep(5)

        # main_page.select_to_station('Фрунзенская')

        # time.sleep(5)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

