Feature: Myntra Beauty End to End Flow

  Scenario Outline: Complete beauty purchase flow
    Given user opens Myntra homepage for end to end
    When user closes popup if present
    And user hovers over beauty menu
    And user selects "Lip Balm" category
    And user opens first product
    And user switches to product tab
    And user selects size if available
    And user adds product to bag
    And user goes to shopping bag
    And user verifies cart item
    And user changes quantity to 2
    And user selects ₹10 donation
    And user clicks place order
    Then user should be redirected to login page
    Examples:
      | category |
      | Lip Balm |
