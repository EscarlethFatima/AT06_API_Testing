Feature: Modify personal information
  Scenario: Add country of origin
    Given I am from Bolivia
    And The zipcode is 0000
    And The number of habitants is:11.145.770
    When I update the information
    Then The information was saved

