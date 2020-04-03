*** Settings ***
Documentation    Suite description

*** Test Cases ***
Test title
    [Tags]    DEBUG
    log to console  pass
    Sleep  5
    log to console  5 sec wait done

