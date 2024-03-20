Feature: User can filter listings using the filter options

  Scenario Outline: 16 - User can filter the Secondary deals by “want to sell” option
    Given Start <browser>. Headless = <headless>
    Then Sign-in Page has opened
    Then Login via Sign-in Page
    Then Click button to open Secondary Listings
    When Secondary Listings Page has opened
    Then Open Secondary Listings filter sidebar
    Then Filter Listings by For Sale
    Then Verify All Listings are for Sale
    Examples:
    | browser   | headless |
    | Chrome    | True     |
    | Chrome    | False    |
    | Firefox   | False    |