from behave import given, when, then


@given('Open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Click terms of service')
def click_tos(context):
    context.app.main_page.click_tos()


@when('Click on "Shop by product" - select Face Washes')
def click_shop_by_prod(context):
    context.app.main_page.click_shop_by_prod()


@then('Verify terms page opened')
def verify_tos_opens(context):
    context.app.main_page.verify_tos_opens()


@then('Verify "Face Wash" is shown')
def verify_face_wash_shown(context):
    context.app.main_page.verify_face_wash_shown()


