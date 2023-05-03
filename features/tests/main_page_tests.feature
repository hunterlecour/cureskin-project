
Feature: Main Page Tests

  Scenario: User can access Terms
    Given Open main page
    When Click on terms of service
    Then Verify Terms of service page opened

  Scenario: User can shop by product Face Washes
    Given Open main page
    When Click on "Shop by product"
    And Click on Face Washes
    Then Verify Face Wash (1) is shown

   Scenario: User can shop by Sunscreens
     Given Open main page
     When Click on "Shop by product"
     And Click on Sunscreens
     And Click on first product
     Then Verify the first product is SPF30 Sunscreen










