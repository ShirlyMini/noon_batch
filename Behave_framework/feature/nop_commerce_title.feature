Feature: Nop Commerce login page title
  Background: steps to implement before each scenario
    Given Launch browser
    When Open Nop Commerce login page

  Scenario: TC1 Verify login page title
    Then Verify Login page title

  Scenario: TC2 Verify Dashboard page
    When Enter Username "admin@yourstore.com" and password "admin"
    And Click Login button
    Then Verify Dashboard page