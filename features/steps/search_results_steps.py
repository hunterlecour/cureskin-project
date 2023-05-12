from behave import given, when, then


@given('Open search result "cure" page')
def open_search_result_cure(context):
    context.app.search_results_page.open_search_result_cure()


@when('Click on CureSkin logo in the header')
def click_logo_header(context):
    context.app.search_results_page.click_logo_header()


@when('Store the name of 1st product and Click on the product')
def store_and_click(context):
    context.app.search_results_page.store_and_click()


@when('Select sort by filter')
def sort_by_filter(context):
    context.app.search_results_page.sort_by_filter()


@when('Select high to low')
def high_to_low(context):
    context.app.search_results_page.high_to_low()


@when('Click on Filter')
def filter_plus(context):
    context.app.search_results_page.filter_plus()


@when('Click on Face Wash (1) and apply')
def face_wash_1(context):
    context.app.search_results_page.face_wash_1()


@when('Click clear all')
def clear_all(context):
    context.app.search_results_page.clear_all()


@when('Verify that {text}')
def verify_face_wash_filter(context, text):
    context.app.search_results_page.verify_face_wash_filter(text)


@then('Verify user is taken to {text}')
def verify_on_main_page(context, text):
    context.app.search_results_page.verify_on_main_page(text)


@then('Verify that {text}')
def verify_23_products(context, text):
    context.app.search_results_page.verify_23_products(text)


@then('Verify product details page opened and product name is correct')
def verify_product_w_details(context):
    context.app.search_results_page.verify_product_w_details()


@then('Verify filter applied (first product price > last product price)')
def verify_high_low(context):
    context.app.search_results_page.verify_high_low()


@then('Verify first results have name, image, and price')
def verify_img_name_price(context):
    context.app.search_results_page.verify_img_name_price()


