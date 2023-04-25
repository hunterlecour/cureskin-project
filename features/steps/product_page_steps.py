from behave import given, when, then


@given('Open Product Details page')
def open_product_page(context):
    context.app.product_page.open_product_page()


@when('Click to add product to cart')
def add_to_cart(context):
    context.app.product_page.add_to_cart()


@when('Verify "added to your cart" confirmation is shown')
def verify_cart_confirm(context):
    context.app.product_page.verify_cart_confirm()


@when('Click "View my cart"')
def view_my_cart(context):
    context.app.product_page.view_my_cart()


@then('Verify user is taken to the cart page')
def verify_cart_page(context):
    context.app.product_page.verify_cart_page()