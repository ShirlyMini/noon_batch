Feature: Nop commerce login Data Driven testing
  Scenario Outline: nop commercer login page test
    Given Launch browser
    When Open Nop Commerce login page
    And Enter Username "<username>" and password "<password>"
    And Click Login button
    Then Verify Dashboard page as per login data "<status>"

    Examples:
    | username              | password  | status  |
    | admin@yourstore.com   | admin     | True    |
    | admin@your12345.com   | admin     | False   |
    | admin@yourstore.com   | adm       | False   |
    | admin@your12345.com   | admin123  | False   |