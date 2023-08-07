from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class RunAutomation:
    """
    The Base Class to be inherited by all other local test classes.
    This Class supplies all the common methods and functions to be used for most test cases.
    Test cases should inherit this Class and use a similar template to run each test.
    Most common actions should be placed here for reuse.

    """
    driver = None
    headless_setting = 'False'
    test_url = 'http://localhost:3000/'
    chromedriver_path = "/usr/bin/chromedriver"

    def browser_setup(self):
        """
        Creates the initial Selenium Webdriver object and sets the Window size and position.

        """
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')

        if self.headless_setting == 'True':
            options.add_argument('headless')
            options.headless = True

        self.driver = webdriver.Chrome(options=options, executable_path=self.chromedriver_path)
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1680, 900)

    def tear_down(self):
        """
        Tears down and closes the browser and driver.

        """
        self.driver.close()

    @staticmethod
    def wait(secs):
        """
        Generates a time to wait in seconds.

        """
        sleep(secs)

    def get_element(self, element_name, search_type="id"):
        """
        Finds a web element by a specified object type.

        """
        if search_type == "name":
            by_type = By.NAME
        elif search_type == "xpath":
            by_type = By.XPATH
        else:
            by_type = By.ID

        return self.driver.find_element(by=by_type, value=element_name)

    def get_all_elements(self, xpath_str='//*', attribute='all'):
        """
        Helper method used for Debugging, can pull and print all elements on the active web page in view.

        """
        print("xpath_str: '%s', attribute: '%s' " % (xpath_str, attribute))

        elems = self.driver.find_elements(By.XPATH, xpath_str)
        for elem in elems:
            if attribute == 'all':
                ats = self.driver.execute_script('var items = {}; for (index = 0; '
                                                 'index < arguments[0].attributes.length; '
                                                 '++index) { items[arguments[0].attributes[index].name] = '
                                                 'arguments[0].attributes[index].value }; return items;', elem)
                print(elem.tag_name + "=" + str(ats))
            else:
                print(elem.tag_name + "=" + elem.get_attribute(attribute))

    @staticmethod
    def send_text_to_element(element, text_to_send, end_with_enter=False):
        """
        Creates the initial Selenium Webdriver object and sets the Window size and position.

        """
        if end_with_enter is True:
            text_to_send = text_to_send + Keys.RETURN

        element.send_keys(text_to_send)

    def wait_for_load(self, timeout_value=30):
        """
        Waits for the loading icon on the page to go away before continuing the test.

        """
        timeout_count = 0
        while timeout_count < timeout_value:
            try:
                elem = self.get_element("//div[@class='circle']", search_type="xpath")
                if elem is None:
                    break
                else:
                    self.wait(1)
                    timeout_count += 1
            except Exception:
                # Loading element likely does not exist, break out
                break

            if timeout_count >= timeout_value:
                assert timeout_count < timeout_value

    def validate_obj_exists(self, element_name, search_type="id"):
        """
        Validates that a web element object exists on the page

        """
        elem = self.get_element(element_name, search_type)
        assert elem is not None
        return elem

    def validate_text_exists(self, text_str, exists=True):
        """
        Validates that text exists (or does not exist) within any object such as a textbox.

        """

        try:
            elem = self.driver.find_element(By.XPATH, "(//*[contains(text(), '" + text_str + "')])")
        except Exception:
            elem = None

        if exists:
            # Validate that text does exist on the page
            assert elem is not None
        else:
            assert elem is None

    @staticmethod
    def validate_obj_property(object_value, value_to_eval):
        """
        Validates that a property value of an object matches the expected value.

        """
        assert object_value == value_to_eval

