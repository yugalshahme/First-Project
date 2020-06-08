*** Settings ***
Documentation    This File Contain All Testing Level Test Cases

*** Test Cases ***
Test for Critical Test Cases
    [Tags]    Critical_test
    log to console  Critical test Started
    Sleep  5
    log to console  Critical test Passed

Test for Smoke Test Cases
    [Tags]    Smoke_Test
    log to console  Smoke Testing Started
    Sleep  5
    log to console  Smoke Testing Passed

Test for Sanity Test Cases
    [Tags]    Sanity_Test
    log to console  Sanity Testing Started
    Sleep  5
    log to console  Sanity Testing Passed

Test for Functional Test Cases
    [Tags]    Functional_Test
    log to console  Functional Testing Started
    Sleep  5
    log to console  Functional Testing Passed
