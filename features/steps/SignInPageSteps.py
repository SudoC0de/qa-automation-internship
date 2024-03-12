from behave import given, when, then


@given('Sign-in Page has opened')
def verify_sign_in_page_opened(context):
    context.app.signin_page.open_signin_page()
    context.app.signin_page.verify_signin_page_opened()

@then('Login via Sign-in Page')
def log_in_via_sign_in_page(context):
    # Assumption is there is a single test user login
    context.app.signin_page.login("functioncf@gmail.com", "#bhqrqC24&MV4zTx")
