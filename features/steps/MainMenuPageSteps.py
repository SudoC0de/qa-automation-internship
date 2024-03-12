from behave import given, when, then


@then("Click button to open Secondary Listings")
def open_secondary_listings(context):
    context.app.main_menu_page.click_secondary_listings_button()
