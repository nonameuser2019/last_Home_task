from SharelineObject import RegisterHelp


def test_reg_shareline(browser):
    main_page = RegisterHelp(browser)
    main_page.go_to_site()
    main_page.enter_signup()
    main_page.enter_zip_code()
    message, message2, message3 = main_page.filling_out_reg_form()
    assert message == 'Account is created!'
    assert len(message2) > 0
    assert len(message3) > 0
