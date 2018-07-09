Feature: Check the money in a account

  Scenario: Withdraw of money in my account
    Given I have $100 in my Account
    When I withdraw $100
    Then I have $0 in my Account