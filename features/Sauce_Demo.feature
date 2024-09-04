Feature:Sauce demo
  Scenario: User successfully logs into the demo application
    Given I am on the Demo Login Page
    When I fill the account information for account StandardUser into the Username field and the password field
    And I click the Login Button
    Then I am redirected to demo main page
    And I verify the App Logo exists

  Scenario: Failed Login
    Given I am on the Demo Login Page
    When I fill the account information for account LockedOutUser into the Username field and the Password field
    And I click the Login Button
    Then I verify the Error Message contains the text "Epic sadface: Sorry, this user has been locked out."

  Scenario: Extract data
    Given I am logged in
    When I am on the inventory page
    Then I extract content from the web page
    And Save it to a text file
    Then I log out
    And I verify I am on the Login page again
