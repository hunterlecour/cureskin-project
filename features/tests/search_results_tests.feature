
Feature: Search Result Tests

  Scenario: Top logo takes to the main page
    Given Open search result "cure" page
    When Click on CureSkin logo in the header
    Then Verify user is taken to https://shop.cureskin.com/

  Scenario: Correct search results are shown
    Given Open search result "cure" page
    Then Verify that 23 results found for “cure”

  Scenario: Search results can be sorted by prices (high - low)
    Given Open search result "cure" page
    When Select sort by filter
    And Select high to low
    Then Verify filter applied (first product price > last product price)

  Scenario: Search results UI is correct
    Given Open search result "cure" page
    Then Verify first results have name, image, and price

  Scenario: Search results filter can be cleared
    Given Open search result "cure" page
    When Click on Filter
    And Click on Face Wash (1) and apply
    And Verify that Product type: Face Wash
    And Click clear all
    Then Verify that 18 results found for “cure”

