Feature: Myntra Beauty Test Cases

  Scenario: Navigate to Beauty Menu
    Given user opens Myntra homepage for test cases
    When user hovers over beauty menu for test cases
    Then Lip Balm category should be visible

  Scenario: Open Product from Homepage
    Given user opens Myntra homepage for test cases
    When user closes popup for test cases
    And user hovers over beauty menu for test cases
    And user opens Lip Balm category for test cases
    And user opens first product for test cases
    Then product page should open

  Scenario: Open Lip Balm Listings
    Given user opens Myntra homepage for test cases
    When user closes popup for test cases
    And user hovers over beauty menu for test cases
    And user opens Lip Balm category for test cases
    Then Lip Balm listing page should open

  Scenario: Add Lip Balm to Cart
    Given user opens Myntra homepage for test cases
    When user hovers over beauty menu for test cases
    And user opens Lip Balm category for test cases
    And user opens third product for test cases
    And user selects size if available for test cases
    And user adds product to bag for test cases
    Then product should be added to cart

  Scenario: Search Invalid Product
    Given user opens Myntra homepage for test cases
    When user searches invalid product
    Then invalid search results should be displayed

  Scenario: Add Product Without Selecting Size
    Given user opens product page
    When user clicks add to bag without selecting size
    Then product should not be added