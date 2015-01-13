import unittest
from selenium import webdriver
import page

class PythonOrgTest(unittest.TestCase):

    def setUp(self):
        
        #Running driver
        
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")

    def test_in_python_org(self):
        
        #Title check
        
        main_page = page.MainPage(self.driver)
        try:
            assert main_page.is_title_matches(), "python.org title doesn't match."
            print ("Title test (PASS)")
        except:
            print ("Title test (FAIL)")
        
        #Searching

        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        try:
            assert search_results_page.is_results_found(), "No results found."
            print ("Page Results (PASS)")
        except:
            print ("Page Results (FAIL)")

        #Jobs check
        
        job_board = page.JobBoard(self.driver)  
        job_board.open_job_page()
        try:
            assert job_board.job_name_find(), "No results found."
            print ("Job Results (PASS)")
        except:
            print ("Job Results (FAIL)")
            

    def tearDown(self):
        
        #Kill driver!
        
        self.driver.close()

if __name__ == "__main__":
    unittest.main()