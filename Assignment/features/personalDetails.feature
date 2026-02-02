Feature: Test cases related to Personal Details


@smoke
Scenario: User can view his profile

    Given user is already logged in
    When user navigate to my profile
    Then user should be able to view his profile


@smoke
Scenario Outline: User can edit personal details

    Given user is already logged in and My Info page
    When user update personal details
    Then successfully updated pop up should come

    Examples:
    | First Name | Middle Name | Last Name |
    | new        | test        | user      |
