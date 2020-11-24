import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import random

import pymongo
import dns
from pymongo import MongoClient

from dotenv import load_dotenv
load_dotenv()

class Crawler:
    def __init__(self, is_headless=False):
        # for more info on arguments, see https://peter.sh/experiments/chromium-command-line-switches/
        # PROXY = '161.202.226.194:8123'
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        # options.add_argument('--proxy-server=%s' % PROXY)
        if is_headless:
            options.add_argument('--headless')
            # options.add_argument('headless')
        self.driver = webdriver.Chrome('./chromedriver', options=options)
        # wait up to 10 seconds for the elements to become available
        self.driver.implicitly_wait(10)

        self.dsi_url = 'http://webscraping-dsi1050.herokuapp.com/login'
        self.ebay_url = 'https://www.ebay.com/'
        self.amazon_url = 'https://www.amazon.com'

        self.static_word = None
        self.dynamic_word = None

        self.__connect_to_db('product_database')

    def __connect_to_db(self, database_name):
        # connect to atlas
        password = os.environ.get('db_password')
        MONGO_URL = f'mongodb+srv://dsi1050:{password}@scraping-data1050.ckqz6.mongodb.net/{database_name}?retryWrites=true&w=majority'

        cluster = MongoClient(MONGO_URL)
        self.db = cluster['product_database']
        self.products = self.db.products
    
    def login(self):
        self.driver.get(self.dsi_url)

        username = self.driver.find_element_by_css_selector('input[type=text]')
        password = self.driver.find_element_by_css_selector('input[type=password]')
        login = self.driver.find_element_by_css_selector('#login-form .button-primary')

        username.send_keys('bruno')
        password.send_keys('Blueno123!')
        login.click()

    def __set_static_word(self):
        # note this renders as such because of the implicitly_wait call in the constructor, 
        # if not, would have to use time.sleep() or something along those lines
        self.static_word = self.driver.find_element_by_css_selector('p:nth-of-type(2)').text.split()[-1]
        print(f'the static word to search for is {self.static_word}')

    def __set_dynamic_word(self):
        time.sleep(1)
        render_word = self.driver.find_element_by_css_selector('button')
        render_word.click()
        # time.sleep(1)
        dynamic_word = self.driver.find_element_by_id('js-val')
        self.dynamic_word = dynamic_word.text.split()[-1]
        print(f'the dynamic word to search for is {self.dynamic_word}')

    def set_static_and_dynamic_words(self):
        self.login()
        self.__set_static_word()
        self.__set_dynamic_word()

    def quit_driver(self):
        self.driver.quit()

    def search_amazon(self, search_input):
        print(f'searching amazon for {search_input}...')
        self.driver.get(self.amazon_url)
        self.__sleep_random_time_interval()
        searchbar = self.driver.find_element_by_css_selector('#twotabsearchtextbox')
        submit = self.driver.find_element_by_css_selector('#nav-search .nav-right .nav-input[type=submit]')
        self.__sleep_random_time_interval()
        searchbar.send_keys(search_input)
        self.__sleep_random_time_interval()
        submit.click()
        self.__sleep_random_time_interval()
        # first_product_url = self.driver.find_element_by_css_selector('.a-link-normal').get_attribute('href')
        first_product_price_element = self.driver.find_element_by_css_selector('.a-price')
        first_product_url = first_product_price_element.find_element_by_xpath('./..').get_attribute('href')
        self.__sleep_random_time_interval()
        self.driver.get(first_product_url)
        price = ''
        product_name = ''
        try:
            price = self.driver.find_element_by_id('priceblock_ourprice').text
            product_name = self.driver.find_element_by_id('productTitle').text.strip()
        except:
            if price == '':
                price = first_product_price_element.text
            if product_name == '':
                product_name = self.driver.find_element_by_css_selector('.qa-title-text').text.strip()
        print('Product name: {}, {}'.format(product_name, price))
        self.__cache_product(product_name, search_input, price)

    def search_ebay(self, search_input):
        print(f'searching ebay for {search_input}...')
        self.driver.get(self.ebay_url)
        self.__sleep_random_time_interval()
        searchbar = self.driver.find_element_by_css_selector('input[type=text]#gh-ac')
        submit = self.driver.find_element_by_css_selector('input[type=submit]#gh-btn')
        self.__sleep_random_time_interval()
        searchbar.send_keys(search_input)
        self.__sleep_random_time_interval()
        submit.click()
        self.__sleep_random_time_interval()
        first_product = self.driver.find_element_by_css_selector('#srp-river-results .s-item')
        product_name = first_product.find_element_by_css_selector('h3').text
        price = first_product.find_element_by_css_selector('.s-item__price').text
        print('Product name: {}, {}'.format(product_name, price))
        self.__cache_product(product_name, search_input, price)

    def __cache_product(self, product_name, product_type, price, print_output=True):
        product_doc = self.products.find_one({"product_name": product_name})
        # see if product already exists
        if product_doc is not None:
            # if product already exists see if this is a cheaper price
            # if is notify user and update lowest/current price
            print(product_doc)
            if price <= product_doc['lowest_price']:
                if (print_output):
                    print('this is the lowest price for product, buy now')
                self.products.update_one(
                    product_doc, {"$set":
                        {
                            "current_price": price, 
                            "lowest_price": price
                        }
                    }
                )
            else:
                if (print_output):
                    print('this is not the lowest price for product, don\'t buy')
                self.products.update_one(
                    product_doc, {"$set":
                        {
                            "current_price": price
                        }
                    }
                )  
            if print_output:
                print("Product '{}' updated in database".format(product_name))
        # if not notify user and update current price
        else:
            if print_output:
                print('adding product into database...')
            product = {
                'product_name': product_name,
                'product_type': product_type,
                'lowest_price': price,
                'current_price': price
            }
            self.products.insert_one(product)
            if print_output:
                print("Product '{}' added to database".format(product_name))

    def run(self):
        pass
        self.set_static_and_dynamic_words()
        self.search_amazon(self.static_word)
        self.search_amazon(self.dynamic_word)
        self.search_ebay(self.static_word)
        self.search_ebay(self.dynamic_word)

    def __sleep_random_time_interval(self):
        time.sleep(random.randint(1,3))


c = Crawler(is_headless=False)
c.run()
c.quit_driver()
