Feature: Create a new gmail account
  Scenario: Create account
    Given I am on the create gmail account page
    And I put Danae Arnez on the name field
    And I put danae123@gmail.com on the user name field
    And I put Testing0- on the password field
    And I put Testing0- on the confirm password field
    And I put 12 15 2000 on the birthdate fields
    And I choose female on the genre field
    And I put 72700000 on the mobile phone field
    When I press on the create button
    Then My new account was created