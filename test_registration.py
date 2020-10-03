from SharelineObject import RegisterHelp


def test_reg_shareline(browser):
    main_page = RegisterHelp(browser)
    main_page.go_to_site()
    main_page.enter_signup()
    main_page.enter_zip_code()
    email, password = main_page.filling_out_reg_form()
    main_page.go_to_site()
    message = main_page.autorization_user(email, password)
    assert len(message) > 0
