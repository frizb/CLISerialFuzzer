# Serial Connection CLI Command Jail Break Fuzzer
# Prerequisite to install pyserial
# python -m pip install pyserial
#
# Created by Austin Scott
# May 3rd, 2018
# Last Updated: May 4th, 2018

# TODO: Account for Blank Responses - Retry test - Retry counter
# TODO: Fix estimated timer.

import serial
import io
import argparse
import time

print('\033[0;32m'+"Serial Connection CLI Command Jail Break Fuzzer : " + '1.0' + " Updated: " + 'May 4, 2018' +'\033[0;39m')
parser = argparse.ArgumentParser(description='Created an ascii file filled with all combinations of HTML escape characters.')
parser.add_argument("-log", type=argparse.FileType("w"),default="log.txt",help='filename to write log output')
parser.add_argument("-testcase", metavar='int', type=int, default=1, help='The test case to resume from (default: %(default)s)')
parser.add_argument("-clicommands", type=argparse.FileType("r"),default="clicommands.txt",help='file containing the cli commands to fuzz')
parser.add_argument("-shellcommands", type=argparse.FileType("r"),default="shellcommands.txt",help='file containing the shell commands to test')
parser.add_argument("-escapecharacters", type=argparse.FileType("r"),default="escapecharacters.txt",help='file containing hex codes for the escape characters to append with CLI and shell commands')
parser.add_argument("-escapecharactercount", metavar='int', type=int, default=1, help='The number of escape characters to combine (default: %(default)s)')
parser.add_argument("-addspace", action='store_true', help='Add a space character between the cli command, the escape character and the shell command.')
parser.add_argument("-success1", type=str, default=":/#", help='The string 1 to look for in output results that could indicate a successful CLI jail break (default: %(default)s)')
parser.add_argument("-success2", type=str, default=":~#", help='The string 2 to look for in output results that could indicate a successful CLI jail break (default: %(default)s)')
parser.add_argument("-success3", type=str, default="root@", help='The string 3 to look for in output results that could indicate a successful CLI jail break (default: %(default)s)')
parser.add_argument("-exception", type=str, default="Exception", help='The string to look for in output results that could indicate an exception (default: %(default)s)')
parser.add_argument("-error", type=str, default="Error", help='The string to look for in output results that could indicate an error (default: %(default)s)')
parser.add_argument("-relogin", type=str, default="login:", help='The string to look for in output results that would require the username and password to be entered (default: %(default)s)')
parser.add_argument("-sudo", type=str, default="password:", help='The string to look for in output results that would require the password to be reentered - like a sudo (default: %(default)s)')
parser.add_argument("-username", type=str, default="admin", help='The username to be used when a login prompt is detected (default: %(default)s)')
parser.add_argument("-password", type=str, default="admin", help='The password to be used when a login prompt / sudo is detected (default: %(default)s)')
parser.add_argument("-com", type=str, default="COM5", help='The Serial COM port to use (default: %(default)s)')
parser.add_argument("-baud", type=int, default=115200, help='The Serial BAUD rate to use (default: %(default)s)')
parser.add_argument("-readtimeout", type=float, default=0.1, help='The Serial read command timeout value to use (default: %(default)s)')
parser.add_argument("-writetimeout", type=float, default=0.1, help='The Serial write command timeout value to use (default: %(default)s)')
parser.add_argument("-interbytetimeout", type=float, default=0.0, help='The Serial inter byte timeout value to use (default: %(default)s)')
parser.add_argument("-parity", type=str, default=serial.PARITY_NONE, help='The Serial parity value to use. Expecting N = PARITY_NONE, E = PARITY_EVEN, O = PARITY_ODD, M = PARITY_MARK or S = PARITY_SPACE (default: %(default)s)')
parser.add_argument("-stopbits", type=int, default=serial.STOPBITS_ONE, help='The Serial stop bits value to use (default: %(default)s)')
parser.add_argument("-bytesize", type=int, default=serial.EIGHTBITS, help='The Serial byte size value to use (default: %(default)s)')
parser.add_argument("-xonxoff", type=int, default=1, help='The Serial xonxoff flag value to use (default: %(default)s)')
parser.add_argument("-rtscts", type=int, default=0, help='The Serial rtscts flag value to use (default: %(default)s)')
parser.add_argument("-dsrdtr", type=int, default=0, help='The Serial dsrdtr flag value to use (default: %(default)s)')
args = parser.parse_args()


def send_command(command, case_num):
    sio.write(unicode(command+"\n"))
    sio.flush()
    try:
        lines = sio.readlines()
        return "".join(lines)
    except Exception as e:
        print "Got something funky! case number: " + str(case_num)
        print "Command: "+command
        print "Exception: " + str(e)
        return "Command: "+command + "\n Case number " + str(case_num)+  " Exception occured!\n"


def escape_char_combine(escape_seq,level):
    level -= 1
    if level == 0:
        escape_seqs.append(escape_seq)
    else:
        for char in escape_chars:
            escape_char_combine(escape_seq+char,level)

try:
    ser = serial.Serial(args.com,
                        args.baud,
                        timeout=args.readtimeout,
                        parity=args.parity,
                        stopbits=args.stopbits,
                        bytesize=args.bytesize,
                        xonxoff=args.xonxoff,
                        rtscts=args.rtscts,
                        dsrdtr=args.dsrdtr,
                        write_timeout=args.writetimeout,
                        inter_byte_timeout=args.interbytetimeout,
                        )
except Exception as e:
    print "Failed to connect to the COM port at : "+args.com
    print " Exception: " + str(e)
    exit(0)

sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

space_char = ""
if args.addspace:
    space_char = " "

# create a list of all possible combinations
commands = []
cli_cmds = []
escape_chars = []
escape_seqs = []
shell_cmds = []
test_case_count = 0

for cli_cmd in args.clicommands:
    cli_cmds.append(cli_cmd)

for escape_char in args.escapecharacters:
    escape_chars.append(chr(int(escape_char,16)))

for char in escape_chars:
    escape_char_combine(char,args.escapecharactercount)

for shell_cmd in args.shellcommands:
    shell_cmds.append(shell_cmd)

# Timing
start_time = time.time()
test_cases_total = len(cli_cmds)*len(escape_seqs)*len(shell_cmds)

for cmd in cli_cmds:
    for char in escape_seqs:
        char_hex = ''.join(["%02X " % ord(x) for x in char]).strip()
        for shell in shell_cmds:
            test_case_count += 1
            if test_case_count < args.testcase: break# Resume Test Case
            # print status update
            if test_case_count % 10 == 0:
                time_per_case = (time.time() - start_time) / test_cases_total
                time_remaining_hours = time_per_case * (test_cases_total - test_case_count)
                print "TEST CASE # " + str(test_case_count) + " OF " + str(test_cases_total) + " - Estimated time remaining: "+ str( time_remaining_hours )

            args.log.write("============================ BEGIN TEST CASE: "+str(test_case_count) + " - escape char HEX: " +char_hex+ " \n")
            time.sleep(2)
            command = cmd.replace("\n", "") + space_char + char + space_char + shell.replace("\n", "") + "\n"
            result = send_command(command,test_case_count)
            if args.success1 in result or args.success2 in result or args.success3 in result:
                args.log.write("SUCCESS!!\n")
                args.log.flush
                print '\033[0;32m' + "Success String found from command (test case # "+str(test_case_count)+") - escape char HEX: " +char_hex+ " "+'\033[0;39m'
                print command
                print "Result Data:"
                print result

            if args.exception in result:
                args.log.write("EXCEPTION!!\n")
                args.log.flush
                print '\033[0;33m' + "Exception String found from command (test case # "+str(test_case_count)+") - escape char HEX: " +char_hex+ " "+'\033[0;39m'
                print command
                print "Result Data:"
                print result

            if args.error in result:
                args.log.write("ERROR!!\n")
                args.log.flush
                print '\033[0;33m' + "Error String found from command (test case # "+str(test_case_count)+") - escape char HEX: " +char_hex+ " "+'\033[0;39m'
                print command
                print "Result Data:"
                print result

            if args.sudo in result:
                args.log.write("SUDO!!\n")
                args.log.flush
                print '\033[0;34m'+"Sudo Password Prompt String found from command (test case # "+str(test_case_count)+") - escape char HEX: " +char_hex+ " "+'\033[0;39m'
                print command
                print "Entering Password..."
                sudo = send_command(args.password, test_case_count)
                time.sleep(1)

            if args.relogin in result:
                args.log.write("RELOGIN!!\n")
                args.log.flush
                print '\033[0;34m'+"Relogin String found from command (test case # "+str(test_case_count)+") - escape char HEX: " +char_hex+ " "+'\033[0;39m'
                print command
                #print "Result Data:"
                #print result
                print "Entering Username and Password..."
                login1 = send_command("", test_case_count)
                time.sleep(1)
                login2 = send_command(args.username, test_case_count)
                time.sleep(1)
                login3 = send_command(args.password, test_case_count)
                time.sleep(1)

            try:
                args.log.write(result+"\n")
                args.log.flush
            except:
                print "Cant write result to log file (test case # "+str(test_case_count)+") - escape char HEX: " +char_hex+ " "+result