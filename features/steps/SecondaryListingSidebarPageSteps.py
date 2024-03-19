from behave import given, when, then

@then('Filter Listings by For Sale')
def filter_listings_by_for_sale(context) -> None:
    context.app.secondary_listings_sidebar_page.wait_until_secondary_listings_sidebar_opened()
    context.app.secondary_listings_sidebar_page.filter_listings_by_sell()
