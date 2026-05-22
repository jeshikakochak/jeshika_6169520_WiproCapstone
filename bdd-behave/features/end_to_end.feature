Feature: Myntra End to End Flow

  Scenario: Complete beauty purchase flow
    Given user opens Myntra homepage
    When user hovers over beauty menu
    And user selects first product
    And user switches to product tab
    And user selects size
    And user clicks add to bag
    Then product should be added successfully