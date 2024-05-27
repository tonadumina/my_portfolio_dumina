import pytest
import pytest_check as check
from tona_project.page.locators import MainPage


def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)

    page.btn_main_header.click()

    elements = [
        (page.btn_headers_present, 'Подарки'),
        (page.btn_headers_new_items, 'Новинки'),
        (page.btn_headers_bags, 'Сумки'),
        (page. btn_headers_for_women, 'Для Женщин'),
        (page.btn_headers_for_men, 'Для Мужчин'),
        (page.btn_headers_jewelry, 'Ювелирные изделия'),
        (page.btn_headers_watch, 'Часы'),
        (page.btn_headers_perfume, 'Парфюм'),
        (page.btn_headers_lifestyle_and_travel, 'Стиль жизни и путешествий'),
        (page.btn_headers_services, 'Услуги'),
        (page. btn_headers_world_louis_vuitton, 'Мир Louis Vuitton'),
    ]

    for elements_btn, elements_text in elements:
        check.is_true(elements_btn.is_visible())
        check.is_true(elements_btn.is_clickable())
        check.equal(elements_btn.get_text(), elements_text)
