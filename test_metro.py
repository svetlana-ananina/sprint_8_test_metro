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

        # Ждем загрузку схемы
        main_page.wait_for_open_main_page()

        main_page.set_field_from('Красные Ворота')
        # main_page.set_field_to('Фрунзенская')

        time.sleep(5)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

