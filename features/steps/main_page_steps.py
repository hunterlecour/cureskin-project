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


@when('Click on Sunscreens')
def click_on_sunscreens(context):
    context.app.main_page.click_on_sunscreens()


@when('Click on first product')
def click_sunscreen_product(context):
    context.app.main_page.click_sunscreen_product()


@when('Click on "Shop by category"')
def click_on_shop_by_cat(context):
    context.app.main_page.click_on_shop_by_cat()


@when('Click on Face')
def click_on_face(context):
    context.app.main_page.click_on_face()


@when("Click on first face product")
def click_on_first_face_product(context):
    context.app.main_page.click_on_first_face_product()


@when('Click on Body')
def click_on_body(context):
    context.app.main_page.click_on_body()


@when('Click on search bar icon')
def search_bar_icon(context):
    context.app.main_page.search_bar_icon()


@when('Click on search bar and input {text}')
def input_text_spf(context, text):
    context.app.main_page.input_text_spf(text)


@when('Click on refund policy')
def click_on_refund_p(context):
    context.app.main_page.click_on_refund_p()


@when('Click on privacy policy')
def click_on_privacy_p(context):
    context.app.main_page.click_on_privacy_p()


@when('Click on shipping policy')
def click_on_shipping_p(context):
    context.app.main_page.click_on_shipping_p()


@when('Click submit')
def click_submit(context):
    context.app.main_page.click_submit()


@when('Verify user is taken to {text}')
def verify_on_face_page(context, text):
    context.app.main_page.verify_on_face_page(text)


@then('Verify {text} page opened')
def verify_tos_opens(context, text):
    context.app.main_page.verify_tos_opens(text)


@then('Verify {text} is shown')
def verify_face_wash_shown(context, text):
    context.app.main_page.verify_face_wash_shown(text)


@then('Verify the first product is {text}')
def verify_first_product_sunscreen(context, text):
    context.app.main_page.verify_first_product_sunscreen(text)


@then('Verify first product name has {text} in it')
def verify_face_product_title(context, text):
    context.app.main_page.verify_face_product_title(text)


@then('Verify the results have {text}')
def verify_spf_shown(context, text):
    context.app.main_page.verify_spf_shown(text)


