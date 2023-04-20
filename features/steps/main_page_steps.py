from behave import given, when, then


@given('Open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Click terms of service')
def click_tos(context):
    context.app.main_page.click_tos()


@then('Verify terms page opened')
def verify_tos_opens(context):
    context.app.main_page.verify_tos_opens()
