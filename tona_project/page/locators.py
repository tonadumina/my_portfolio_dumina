import os

from tona_project.page.base_page import WebPage
from tona_project.page.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ru.louisvuitton.com/rus-ru/homepage'

        super().__init__(web_driver, url)

    #кнопка открытия меню(headers)
    btn_main_header = WebElement(id="mobile-menu-toggler")

    #headers
    btn_headers_present = WebElement(xpath='//*[@id="nvcat3470005v-button"]')
    btn_headers_new_items = WebElement(xpath='//*[@id="nvcat1830004v-button"]')
    btn_headers_bags = WebElement(xpath='//*[@id="nvcat3250018v-button"]')
    btn_headers_for_women = WebElement(xpath='//*[@id="femme-button"]')
    btn_headers_for_men = WebElement(xpath='//*[@id="homme-button"]')
    btn_headers_jewelry = WebElement(xpath='//*[@id="nvcat3250005v-button"]')
    btn_headers_watch = WebElement(xpath='//*[@id="nvcat3250009v-button"]')
    btn_headers_perfume = WebElement(xpath='//*[@id="nvcat3250014v-button"]')
    btn_headers_lifestyle_and_travel = WebElement(xpath='//*[@id="nvcat1840004v-button"]')
    btn_headers_services = WebElement(xpath='//*[@id="nvcat3330002v-button"]')
    btn_headers_world_louis_vuitton = WebElement(xpath='//*[@href="/rus-ru/magazine"]/span')

    #footers
    btn_footer_questions = WebElement(xpath='//*[@href="/rus-ru/faq" and contains(text(),"Часто задаваемые вопросы")]')
    btn_footer_shops = WebElement(xpath='//*[@href="/rus-ru/stores" and contains(text(),"Магазины")]')
    btn_footer_delivery_and_returns = WebElement(xpath='//*[@href="/rus-ru/faq" and contains(text(),"Условия доставки и возврата")]')
    btn_footer_product_repair = WebElement(xpath='//*[@href="/rus-ru/care-service" and contains(text()," Ремонт изделий")]')
    btn_footer_personalization = WebElement(xpath='')





