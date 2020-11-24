from selenium import webdriver                   
from selenium.webdriver.common.keys import Keys   
import time

URL = 'http://books.toscrape.com/'


def scrape_page(driver):
    # get the titles, prices, ratings and availabilities for each book through css selection
    titles = [ web_element.text for web_element in driver.find_elements_by_css_selector('.product_pod > h3 > a') ]
    prices = [ web_element.text for web_element in driver.find_elements_by_css_selector('.product_pod .price_color') ]
    ratings = [ web_element.get_attribute('class').split()[1] for web_element in driver.find_elements_by_css_selector('.product_pod .star-rating')]
    avalabilities = [ web_element.text.strip() for web_element in driver.find_elements_by_css_selector('.availability')]

    # highlight first selection of each (not necessary but helpful to show how to manipulate page)
    titleDivs = driver.find_elements_by_css_selector('.product_pod > h3 > a')
    priceDivs = driver.find_elements_by_css_selector('.product_pod .price_color')
    ratingDivs = driver.find_elements_by_css_selector('.product_pod .star-rating')
    avalabilityDivs = driver.find_elements_by_css_selector('.availability')
    for info in zip(titleDivs, priceDivs, ratingDivs, avalabilityDivs):
        driver.execute_script("arguments[0].setAttribute('style', 'color: black; border: 2px solid green; background-color: yellow;')", info[0])
        driver.execute_script("arguments[0].setAttribute('style', 'color: black; border: 2px solid blue; background-color: yellow;')", info[1])
        driver.execute_script("arguments[0].setAttribute('style', 'color: black; border: 2px solid red; background-color: yellow;')", info[2])
        driver.execute_script("arguments[0].setAttribute('style', 'color: black; border: 2px solid purple; background-color: yellow;')", info[3])

    # setAttribute(element, "style",
    #              "color: black; border: 5px solid black; background-color: yellow;")

    for relevant_info in zip(titles, prices, ratings, avalabilities):
        print(f'title: {relevant_info[0]}, price: {relevant_info[1]}, rating: {relevant_info[2]}, availability: {relevant_info[3]}')



def scrape_all_pages(URL, highlight_just_first_page=False):
    # to install chromedriver, see https://chromedriver.chromium.org/downloads
    driver = webdriver.Chrome('./chromedriver')
    driver.get(URL)
    next_buttons = driver.find_elements_by_css_selector('.next a')
    driver.execute_script("arguments[0].setAttribute('style', 'color: black; border: 2px solid green; background-color: yellow;')", next_buttons[0])

    if (not highlight_just_first_page):
        while len(next_buttons) > 0:
            scrape_page(driver)
            next_page_url = next_buttons[0].get_attribute('href')
            # go to next page (the link provided by the href)
            driver.get(next_page_url)
            next_buttons = driver.find_elements_by_css_selector('.next a')

    scrape_page(driver)
    time.sleep(10)
    driver.quit()
    

scrape_all_pages(URL, highlight_just_first_page=True)
scrape_all_pages(URL)
