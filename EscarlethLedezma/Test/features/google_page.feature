Feature: Verification of the google main page
  This feature contains all the required scenarios to verify that the google main page
  works correctly

  Scenario: Search verifying components
    Given I am on the google main page
    And I can see the Google logo
    And I can see the toolbar
    And I can put a search on the search input
    When I click on search button
    Then I can see the search results page

  Scenario: File search with Google Search
    Given I am on the google main page
    When I put the search on the search input
    And I press the Google Search button
    Then I can see a list with all search results

  Scenario: File search with I'm feeling lucky
    Given I am on the google main page
    When I put the search on the search input
    And I press the I'm feeling lucky button
    Then I am redirected to the page of the first search result.

  Scenario: File search with empty search
    Given I am on the google main page
    When  I leave empty the search input
    And I press the Search button
    Then I stay on the same page

  Scenario: Change the language
    Given I am on the google main page
    When  I click on the "Google is offered in: English" button
    Then I can see all the names on the page were changed

  Scenario: Sign in using toolbar button
    Given I am on the google main page
    When  I click on the "Sign in" button
    Then I am redirected to google account access page

  Scenario: Redirect to gmail using toolbar button
    Given I am on the google main page
    When  I click on the "Gmail" button
    Then I am redirected to google account access page

  Scenario: Redirect to Google Images using toolbar button
    Given I am on the google main page
    When  I click on the "Images" button
    Then I am redirected to google images page

  Scenario: Select google functionalities
    Given I am on the google main page
    When  I click on the selector button on the toolbar
    And I can see a list with google functionalities
    Then I can choose a google functionality