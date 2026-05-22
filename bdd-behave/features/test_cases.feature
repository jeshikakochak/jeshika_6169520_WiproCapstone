Feature: Myntra Negative Test Cases

  Scenario: Search invalid product
    Given user opens Myntra homepage
    When user searches for invalid product
    Then invalid search results should be displayed

  Scenario: Add product without selecting size
    Given user opens product page
    When user clicks add to bag without selecting size
    Then product should not be added