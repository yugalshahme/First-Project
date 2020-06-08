*** Settings ***
Documentation    This File Contain All Testing Level Test Cases

*** Test Cases ***
Test for Critical Test Case
    [Tags]    Critical_test
    log to console  Critical Tests Started
    Sleep  5
    log to console  Critical Tests Passed

Test for Smoke Test Case
    [Tags]    Smoke_Test
    log to console  Smoke Tests Started
    Sleep  5
    log to console  Smoke Tests Passed

Test for Sanity Test Case
    [Tags]    Sanity_Test
    log to console  Sanity Tests Started
    Sleep  5
    log to console  Sanity Tests Passed

Test for Functional Test Case
    [Tags]    Functional_Test
    log to console  Functional Tests Started
    Sleep  5
    log to console  Functional Tests Passed
