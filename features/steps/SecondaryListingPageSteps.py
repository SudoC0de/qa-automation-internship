from behave import given, when, then


@when('Secondary Listings Page has opened')
def verify_secondary_listings_page_opened(context) -> None:
    context.app.secondary_listings_page.verify_secondary_listings_opened()

@then('Open Secondary Listings filter sidebar')
def open_secondary_listings_filter_sidebar(context) -> None:
    context.app.secondary_listings_page.click_filter_button()

@then('Verify All Listings are for Sale')
def verify_all_listings_are_for_sale(context) -> None:
    context.app.secondary_listings_page.verify_listings_for_sales()
