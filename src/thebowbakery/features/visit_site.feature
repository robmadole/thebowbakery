Feature: See a list of bows I can purchase
    In order to buy a bow I like
    As a visitor to thebowbakery.com
    I want to be able to see a list of available bows

Background:
    Given test data named 'test_bows' is loaded

Scenario: Redirects to correct URL
    When I visit 'thebowbakery.com'
    Then I should be redirected to 'thebowbakery.com/bows'

Scenario: Free shipping
    When I visit 'thebowbakery.com'
    Then I should see a message telling me 'Free Shipping in the U.S.'

Scenario: See a list of bows
    When I visit 'thebowbakery.com/bows'
    Then I should see 7 bows with add buttons

Scenario: Someone purchases the last bow
    Given that bow 'B1' has been purchased
    When I visit 'thebowbakery.com/bows'
    Then I should see 6 bows with add buttons
