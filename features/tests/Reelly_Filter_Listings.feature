Feature: User can filter listings using the filter options

  Scenario: 16 - User can filter the Secondary deals by “want to sell” option
    Given Sign-in Page has opened
    Then Login via Sign-in Page
    Then Click button to open Secondary Listings
    When Secondary Listings Page has opened
    Then Open Secondary Listings filter sidebar
    Then Filter Listings by For Sale
    Then Verify All Listings are for Sale