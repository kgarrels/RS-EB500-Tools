### long time ago
    - 4-55 received from R&S. USB/LSB demodulation broken. Downgraded to 4.50.
    - running 4.56 
    - Seldom lock-ups of the receiver, generates humm, no ifpanel or iq streams. Lock-up can be ended with a short test.
### 2016-03-19
    - Downgraded receiver to 4.50.
    - Informed R&D Customer Support, promised to send an answer after easter.
### 2016-04-24
    - upgraded to 4.56 again
    - internal GUI lost connection to receiver, both run, but manual operation does not go through. Remote GUI still works as normal
### 2016-05-01
    - lock-up again, downgraded to 4.50
    - again internal communication loss with error message from gui ;-(
### 2016-05-05
    - CAT5 cable from FP to receiver was not klicked in. Fixed.
### 2016-05-16
    - discovered ftp access in antenna correction factor manual, user: EB500, pwd: EB500
    - also works for telnet, then some consolse commands are available, try "help"
    - "rld" displays a ramlog, monitoring everything that is going on in the receiver
### 2016-06-05
    - what really happens when the front pannel stalls:
        - the receiver still works without problems from remote
        - the ramlog does not show anything special
        - the front panel display follows the receiver
        - input from front panel is ignored
        - after some time, the input is processed
### 2016-06-19
    - now disassembled also the fronst panel PC, cleaned RJ45 connection with air
    - since then, np more drops of eth0 in ramlog, and no more interruptions of internal gui
     
    



