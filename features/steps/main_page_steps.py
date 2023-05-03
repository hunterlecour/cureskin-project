from behave import given, when, then


@given('Open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Click on terms of service')
def click_on_tos(context):
    context.app.main_page.click_on_tos()


@when('Click on "Shop by product"')
def click_shop_by_prod(context):
    context.app.main_page.click_shop_by_prod()


@when('Click on Face Washes')
def click_on_face_washes(context):
    context.app.main_page.click_on_face_washes()


@then('Verify terms page opened')
def verify_tos_opens(context):
    context.app.main_page.verify_tos_opens()


@then('Verify "Face Wash" is shown')
def verify_face_wash_shown(context):
    context.app.main_page.verify_face_wash_shown()


