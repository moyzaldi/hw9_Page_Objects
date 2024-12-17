from resources.users import new_user
from demoqa_automation_practice_form.registration_page import RegistrationPage, TableResponsive


def test_registration_user(browser_settings):

    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.remove_banner()
    registration_page.fill_first_name(new_user.first_name)
    registration_page.fill_last_name(new_user.last_name)
    registration_page.fill_email(new_user.user_email)
    registration_page.fill_gender(new_user.gender)
    registration_page.fill_mobile(new_user.user_number)
    registration_page.fill_date_of_birth(new_user.month, new_user.year, new_user.day)
    registration_page.fill_subject(new_user.subjects)
    registration_page.fill_hobby(new_user.hobbies)
    registration_page.up_load_picture(new_user.images)
    registration_page.fill_current_address(new_user.current_address)
    registration_page.fill_state(new_user.state)
    registration_page.fill_city(new_user.city)
    registration_page.submit()

    table_responsive = TableResponsive()

    table_responsive.assert_full_name(new_user.first_name, new_user.last_name)
    table_responsive.assert_userEmail(new_user.user_email)
    table_responsive.assert_gender(new_user.gender)
    table_responsive.assert_userNumber(new_user.user_number)
    table_responsive.assert_date_of_birth(new_user.day, new_user.month, new_user.year)
    table_responsive.assert_subjects(new_user.subjects)
    table_responsive.assert_hobbies(new_user.hobbies)
    table_responsive.assert_images(new_user.images)
    table_responsive.assert_currentAddress(new_user.current_address)
    table_responsive.assert_state_and_city(new_user.state, new_user.city)