
Feature: Main Page Tests

  Scenario: User can access Terms
    Given Open main page
    When Click terms of service
    Then Verify terms page opened

  Scenario: Top logo takes to the main page
    Given Open search results page
    When Click on CureSkin logo in the header
    Then Verify user is taken to the main page