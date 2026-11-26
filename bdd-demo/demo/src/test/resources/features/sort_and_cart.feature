Feature: Sort products and add items to cart
  @smoke
  Scenario: Sort products by price and add the first two items to cart
    Given I am on the login page
    And I have logged in with username "standard_user" and password "secret_sauce"
    When I sort products by price from low to high
    And I add the first 2 products to the cart
    And I open the shopping cart
    Then I should see 2 items in the cart
