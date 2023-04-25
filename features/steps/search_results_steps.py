from behave import given, when, then


@given('Open search result "cure" page')
def open_search_result_cure(context):
    context.app.search_results_page.open_search_result_cure()


@when('Click on CureSkin logo in the header')
def click_logo_header(context):
    context.app.search_results_page.click_logo_header()


@then('Verify user is taken to the main page')
def verify_on_main_page(context):
    context.app.search_results_page.verify_on_main_page()


@then('Verify that 23 products are returned')
def verify_23_products(context):
    context.app.search_results_page.verify_23_products()


