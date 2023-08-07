from baseclass import RunAutomation


class TestApp(RunAutomation):

    def test_begin(self):
        self.browser_setup()
        self.perform_user_actions()

    def perform_user_actions(self):
        self.driver.get(self.test_url)
        # Validate page title
        self.validate_obj_property(self.driver.title, "Get Github Repos")
        # Validate search bar exists
        search_bar = self.validate_obj_exists("username", search_type="id")
        # Validate Go button exists
        button_elem = self.validate_obj_exists("//*[contains(text(),'Go')]", search_type="xpath")

        # Attempt to query for user and wait for page to load
        self.send_text_to_element(search_bar, "Xeal", end_with_enter=True)
        self.wait_for_load()
        # Validate success message
        self.validate_text_exists("Success")
        # Validate item in table is a clickable link
        self.validate_obj_exists("//a[@href='https://github.com/xeal/dotfiles']", search_type="xpath")
        # Validate item description is blank
        self.validate_obj_exists("//main/section[2]/div/ul/li/p[2][contains(text(),'–')]", search_type="xpath")

        # Attempt to query for a second user
        search_bar.clear()
        self.send_text_to_element(search_bar, "Rabbearsu", end_with_enter=False)
        button_elem.click()

        self.wait_for_load()
        # Validate success message
        self.validate_text_exists("Success")
        # Validate item in table is a clickable link
        self.validate_obj_exists("//main/section[2]/div/ul/li[1]/p[1]/a[contains(@href,'Notes-Chinese')]", "xpath")
        # Validate item description with chinese characters
        self.validate_obj_exists("//main/section[2]/div/ul/li[1]/p[2][contains(text(),'2018/2019/校')]", "xpath")


if __name__ == '__main__':
    TestApp().test_begin()
