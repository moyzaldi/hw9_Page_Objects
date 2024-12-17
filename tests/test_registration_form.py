from demoqa_automation_practice_form.registration_page import RegistrationPage, TableResponsive
from resources import users


def test_registration_user(browser_settings):
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.remove_banner()
    registration_page.register(users.new_user)

    table_responsive = TableResponsive()
    table_responsive.assert_data(users.new_user)
