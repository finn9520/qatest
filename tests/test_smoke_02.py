from baseclass import RunAutomation


class TestApp(RunAutomation):

    def test_begin(self):
        self.browser_setup()
        self.perform_user_actions()

    def perform_user_actions(self):
        self.driver.get(self.test_url)
        # Validate search bar exists
        search_bar = self.get_element("username", search_type="id")

        # Attempt to query for an empty field
        search_bar.clear()
        self.send_text_to_element(search_bar, "", end_with_enter=True)
        self.wait_for_load()
        # Validate success message
        self.validate_text_exists("Github user not found")
        # Validate item in table is a clickable link
        self.validate_obj_exists("//*[contains(text(),'No repos')]", search_type="xpath")

        self.wait(3)
        # Attempt to query a non-existent user
        search_bar.clear()
        self.send_text_to_element(search_bar, "Thisuserdoesnotexisthere", end_with_enter=True)
        self.wait_for_load()
        # Validate success message
        self.validate_text_exists("Github user not found")
        # Validate item in table is a clickable link
        self.validate_obj_exists("//*[contains(text(),'No repos')]", search_type="xpath")

        self.wait(3)
        # Attempt to query invalid characters
        search_bar.clear()
        self.send_text_to_element(search_bar, "^!%#R&(*^&)", end_with_enter=True)
        self.wait_for_load()
        self.wait(2)
        # Validate success message
        self.validate_text_exists("Something went wrong")
        # Validate item in table is a clickable link
        self.validate_obj_exists("//*[contains(text(),'No repos')]", search_type="xpath")


if __name__ == '__main__':
    TestApp().test_begin()
