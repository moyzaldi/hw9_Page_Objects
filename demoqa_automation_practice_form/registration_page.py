import os

from selene import browser, by, have


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_mobile(self, value):
        browser.element('#userNumber').type(value)

    def fill_gender(self, value):
        browser.element('#genterWrapper').element(by.text(value)).click()

    def fill_date_of_birth(self, mm, yyyy, dd):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(mm)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(yyyy)).click()
        if len(dd) == 1:
            dd = '0' + dd
        browser.element(f'.react-datepicker__day--0{dd}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobby(self, value):
        browser.element('#hobbiesWrapper').element(by.text(value)).click()

    def up_load_picture(self, path):
        browser.element("#uploadPicture").send_keys(os.path.abspath(f"../resources/images/{path}"))

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, value):
        browser.element('#state').click().element(by.text(value)).click()

    def fill_city(self, value):
        browser.element('#city').click().element(by.text(value)).click()

    def submit(self):
        browser.element('#submit').click()


class TableResponsive:

    def assert_full_name(self, firstName,lastName):
        browser.element('.table-responsive').should(have.text(f'{firstName} {lastName}'))

    def assert_userEmail(self, userEmail):
        browser.element('.table-responsive').should(have.text(userEmail))

    def assert_gender(self, gender):
        browser.element('.table-responsive').should(have.text(gender))

    def assert_userNumber(self, userNumber):
        browser.element('.table-responsive').should(have.text(userNumber))

    def assert_date_of_birth(self, day, month,year):
        browser.element('.table-responsive').should(have.text(f'{day} {month},{year}'))

    def assert_subjects(self, subjects):
        browser.element('.table-responsive').should(have.text(subjects))

    def assert_hobbies(self, hobbies):
        browser.element('.table-responsive').should(have.text(hobbies))

    def assert_images(self, images):
        browser.element('.table-responsive').should(have.text(images))

    def assert_currentAddress(self, currentAddress):
        browser.element('.table-responsive').should(have.text(currentAddress))

    def assert_state_and_city(self, state, city):
        browser.element('.table-responsive').should(have.text(f'{state} {city}'))