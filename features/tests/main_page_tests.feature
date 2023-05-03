
Feature: Main Page Tests

  Scenario: User can access Terms
    Given Open main page
    When Click on terms of service
    Then Verify terms page opened

  Scenario: User can shop by product Face Washes
    Given Open main page
    When Click on "Shop by product"
    And Click Face Washes
    Then Verify "Face Wash" is shown









