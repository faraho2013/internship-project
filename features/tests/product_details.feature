Feature: Tests for product page

  Scenario: User can open product detail and see three options of visualization
    Given Open reely main page
    When Login to the page with email and password
    And Click on “off plan" at the left side menu
    And Click on first off plan product
    Then  Verify one of the three options is available
    Then  Verify the visualization options are clickable