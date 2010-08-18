Feature: Get support
    In order to get support
    As a visitor to thebowbakery.com
    I want the ability to contact the site owners
        
Scenario: Email support
    When I visit 'thebowbakery.com/bows'
    And I click the link 'help@thebowbakery.com'
    Then I should see a new email message window
    And the To: field should be 'help@thebowbakery.com'
