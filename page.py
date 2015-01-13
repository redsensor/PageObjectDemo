from element import BasePageElement
from locators import MainPageLocators 
import time

class SearchTextElement(BasePageElement):

    locator = 'q'

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Welcome to Python.org" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):

    def is_results_found(self):

        return "Australia" in self.driver.page_source 
    
class JobBoard(BasePage):
    
    def open_job_page(self):
        self.driver.find_element_by_link_text('Jobs').click()
        time.sleep(3)
        
    def job_name_find(self):
        return "Python developer" in self.driver.page_source      