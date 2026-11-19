# src/test/resources/features/login.feature   (final version for Handout 2)
Feature: Log in to Swag Labs
  Shoppers must log in before they can see the products.
  Only known, unlocked users with the shared password get in.

  Scenario: Valid user logs in
    Given I am on the login page
    When I log in with username "standard_user" and password "secret_sauce"
    Then I should see the "Products" page

  Scenario: Locked-out user is refused
    Given I am on the login page
    When I log in with username "locked_out_user" and password "secret_sauce"
    Then I should see the error "Epic sadface: Sorry, this user has been locked out."

  Scenario: Wrong password is refused
    Given I am on the login page
    When I log in with username "standard_user" and password "wrong_sauce"
    Then I should see the error "Epic sadface: Username and password do not match any user in this service"


  Scenario: Logged-in user logs out
    Given I am on the login page
    And I have logged in with username "standard_user" and password "secret_sauce"
    When I log out
    Then I should be back on the login page