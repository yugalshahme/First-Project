*** Settings ***
Documentation    Suite description

*** Test Cases ***
Test title
    [Tags]    DEBUG
    log to console  pass
    Sleep  5
    log to console  5 sec wait done

Test title with Error
    [Tags]    DEBUG1
    log to console  pass
    Sleep  5
    log not to console  5 sec wait done
