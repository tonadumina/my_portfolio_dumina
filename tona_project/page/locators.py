import os

from tona_project.page.base_page import WebPage
from tona_project.page.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://alex-zoo.by/'

        super().__init__(web_driver, url)

    btn_headers_catalog = WebElement(xpath='/html/body/div[3]/header/div/div[3]/div/div/div[2]/div/nav/ul/li[1]/a')
    btn_headers_delusions = WebElement(xpath='/html/body/div[3]/header/div/div[3]/div/div/div[2]/div/nav/ul/li[2]/a')
    btn_headers_vlog = WebElement(xpath='//html/body/div[3]/header/div/div[3]/div/div/div[2]/div/nav/ul/li[3]/a')
    btn_headers_contacts = WebElement(xpath='/html/body/div[3]/header/div/div[3]/div/div/div[2]/div/nav/ul/li[4]/a')
    btn_headers_delivery = WebElement(xpath='//html/body/div[3]/header/div/div[3]/div/div/div[2]/div/nav/ul/li[5]/a')
    btn_headers_stock = WebElement(xpath='/html/body/div[3]/header/div/div[3]/div/div/div[2]/div/nav/ul/li[6]/a')