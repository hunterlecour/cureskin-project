
Feature: Search Result Tests

  Scenario: Top logo takes to the main page
    Given Open search result "cure" page
    When Click on CureSkin logo in the header
    Then Verify user is taken to the main page
