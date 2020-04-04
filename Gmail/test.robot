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
    log to console  5 sec wait done

Test title1
    [Tags]    DEBUG
    log to console  pass
    Sleep  5
    log to console  5 sec wait done

Test title with Error1
    [Tags]    DEBUG1
    log to console  pass
    Sleep  5
    log to console  5 sec wait done
    
Test title2
    [Tags]    DEBUG
    log to console  pass
    Sleep  5
    log to console  5 sec wait done

Test title with Error2
    [Tags]    DEBUG1
    log to console  pass
    Sleep  5
    log to console  5 sec wait done

Test title3
    [Tags]    DEBUG
    log to console  pass
    Sleep  5
    log to console  5 sec wait done

Test title with Error3
    [Tags]    DEBUG1
    log to console  pass
    Sleep  5
    log to console  5 sec wait done

Test title4
    [Tags]    DEBUG
    log to console  pass
    Sleep  5
    log to console  5 sec wait done

Test title with Error4
    [Tags]    DEBUG1
    log to console  pass
    Sleep  5
    log not to console  5 sec wait done
