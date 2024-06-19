import time

import allure
import pytest_check as check
from page.locators import MainPage


@allure.story('Главная страница')
@allure.feature('Проверка хедара')
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
        with allure.step('Проверка отображения'):
            check.is_true(elements_btn.is_visible())
        with allure.step('Проверка кликабельость'):
            check.is_true(elements_btn.is_clickable())
        with allure.step('Проверка текста'):
            check.equal(elements_btn.get_text(), elements_text)


@allure.story('Главная страница')
@allure.feature('Проверка футера')
def test_footers(web_browser):
    """Этот тест проверяет футер главной страницы"""

    page = MainPage(web_browser)

    elements = [
         (page.btn_footer_questions, 'Часто задаваемые вопросы'),
         (page.btn_footer_product_care, 'Уход за изделиями'),
         (page.btn_footer_shops, 'Магазины'),
         (page.btn_footer_delivery_and_returns, 'Условия доставки и возврата'),
         (page.btn_footer_product_repair, 'Ремонт изделий'),
         (page.btn_footer_personalization, 'Персонализация'),
         (page.btn_footer_give_gifts, 'Искусство дарить подарки'),
         (page.btn_footer_fashion, 'Мода'),
         (page.btn_footer_arts_and_culture, 'Искусство и культура'),
         (page.btn_footer_home_louis_vuitton, 'Дом Louis Vuitton'),
         (page.btn_footer_sustainable_development, 'Устойчивое развитие'),
         (page.btn_footer_last_news, 'Последние новости'),
         (page.btn_footer_vacancies, 'Вакансии'),
         (page.btn_footer_fund_louis_vuitton, 'Фонд Louis Vuitton'),
         (page.btn_footer_register, 'Зарегистрируйтесь'),
     ]

    for elements_btn, elements_text in elements:
        with allure.step('Проверка отображения'):
            check.is_true(elements_btn.is_visible())
        with allure.step('Проверка кликабельность'):
            check.is_true(elements_btn.is_clickable())
        with allure.step('Проверка текста'):
            check.equal(elements_btn.get_text(), elements_text)


@allure.story('Главная страница')
@allure.feature('Проверка поиска')
def test_search(web_browser):
    """Этот тест проверяет поиск на главной страницы"""

    page = MainPage(web_browser)

    with allure.step('Нажимаем на кнопку поиска'):
        page.btn_headers_headerSearchButton.click()
        time.sleep(2)

    with allure.step('Нажимаем на кнопку поиска'):
        page.btn_headers_searchHeaderInput.send_keys('Женские сумки')
        time.sleep(5)

