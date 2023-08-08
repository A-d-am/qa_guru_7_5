import os

from selene import browser, have, be

def test_fill_and_send_form():
    browser.open('/automation-practice-form')
    # first name
    browser.element('#firstName').should(be.blank).type('FirstName')
    # last name
    browser.element('#lastName').should(be.blank).type('LastName')
    # email
    browser.element('#userEmail').should(be.blank).type('username@domain.com')
    # gender
    browser.element('[for="gender-radio-1"]').should(have.text('Male')).click()
    # mobile phone (10 digits)
    browser.element('#userNumber').should(be.blank).type('1234567890')
    # date of birth
    """ 
    тут нашел интересную особенность: если очистить поле с помощью 
    browser.element('#dateOfBirthInput').click().clear() , 
    то вместо страницы с формой появляется белый экран
    Аналогично, если удалить все с помощью backspace 
    """
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__month-select > option[value='4']").click()
    browser.element(".react-datepicker__year-select > option[value='2000']").click()
    browser.element('.react-datepicker__day--017').click()

    # subjects
    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    browser.element('#subjectsInput').should(be.blank).type('Hindi').press_enter()
    # hobbies
    browser.element('.custom-checkbox [for = "hobbies-checkbox-1"]').should(have.text('Sports')).click()
    # upload picture
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/test_pict.png'))
    # current address
    browser.element('#currentAddress').should(be.blank).type('Current address').press_enter()
    # state
    browser.element('#react-select-3-input').type('NCR').press_enter()
    # city
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    # click on submit button
    browser.element('#submit').click()
    # check results
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tbody > tr').first.should(have.text('Student Name FirstName LastName'))
    browser.all('tbody > tr').second.should(have.text('Student Email username@domain.com'))
    browser.all('tbody > tr')[2].should(have.text('Gender Male'))
    browser.all('tbody > tr')[3].should(have.text('Mobile 1234567890'))
    browser.all('tbody > tr')[4].should(have.text('Date of Birth 17 May,2000'))
    browser.all('tbody > tr')[5].should(have.text('Subjects Maths, Hindi'))
    browser.all('tbody > tr')[6].should(have.text('Hobbies Sports'))
    browser.all('tbody > tr')[7].should(have.text('Picture test_pict.png'))
    browser.all('tbody > tr')[8].should(have.text('Address Current address'))
    browser.all('tbody > tr')[-1].should(have.text('State and City NCR Delhi'))
