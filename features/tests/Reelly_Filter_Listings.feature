Feature: User can filter listings using the filter options

  Scenario Outline: 16 - User can filter the Secondary deals by “want to sell” option
    Given Start <browser>. Headless = <headless>, Remote = <remote>, RemoteOS = <remote_os>, RemoteOSVer = <remote_os_ver>
    Then Sign-in Page has opened
    Then Login via Sign-in Page
    Then Click button to open Secondary Listings
    When Secondary Listings Page has opened
    Then Open Secondary Listings filter sidebar
    Then Filter Listings by For Sale
    Then Verify All Listings are for Sale
    Examples:
    | browser   | headless | remote | remote_os | remote_os_ver |
    | Chrome    | False    | False  | None      | None          |
    | Firefox   | False    | False  | None      | None          |