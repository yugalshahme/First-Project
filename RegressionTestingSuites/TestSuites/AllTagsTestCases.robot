*** Settings ***
Documentation    This File Contain All Testing Level Test Cases

*** Test Cases ***
Test for Critical Test Case
    [Tags]    Critical_test
    log to console  Critical Test Started
    Sleep  5
    log to console  Critical Test Passed

Test for Smoke Test Case
    [Tags]    Smoke_Test
    log to console  Smoke Test Started
    Sleep  5
    log to console  Smoke Test Passed

Test for Sanity Test Case
    [Tags]    Sanity_Test
    log to console  Sanity Test Started
    Sleep  5
    log to console  Sanity Test Passed

Test for Functional Test Case
    [Tags]    Functional_Test
    log to console  Functional Test Started
    Sleep  5
    log to console  Functional Test Passed
