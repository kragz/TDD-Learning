from selenium import webdriver
from selenium.webdriver.common.keys  import Keys 
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #John has heard about a cool new online to-do app. He goes 
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-do', header_text)

        #He is ivets to enter a to-do item staright away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input.get_attribute('placehoder'),
            'Enter a to-do item'
        )

        #he types "buy peacock feathers" into a text box(Edith's hobby )
        # is typng fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When he hits enter, tehe page updates, and now the page lists 
        # "1: Buy peacock feathers" as an item in a to-do list table 
        input.send_keys(Keys.ENTER)
        time.sleep()

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag('tr')
        self.asserTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
         
        self.fail('Finish the test!')
        
if __name__ == "__main__":
    unittest.main(warnings='ignore')


'''browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'To-Do' in browser.title, "Browser title was " + browser.title

browser.quit()'''

