from behave import given, when, then


@given('Open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@given('Open search results page')
def open_search_result(context):
    context.app.main_page.open_search_result()


@when('Click terms of service')
def click_tos(context):
    context.app.main_page.click_tos()


@when('Click on CureSkin logo in the header')
def click_logo_header(context):
    context.app.main_page.click_logo_header()


@then('Verify terms page opened')
def verify_tos_opens(context):
    context.app.main_page.verify_tos_opens()


@then('Verify user is taken to the main page')
def verify_on_main_page(context):
    context.app.main_page.verify_on_main_page()
