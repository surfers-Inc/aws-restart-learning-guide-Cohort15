import os
import subprocess # subprocces module can be used to spawn ne processes


os.system("ls") # takes in string argument
# run ls command using subprocess
subprocess.run(["ls"])

#subprocess with two arguments
subprocess.run(["ls","-l"])

#subprocess with three arguments
subprocess.run(["ls","-l","README.md"]) 

# retrive system info
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

#Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])










# The full list of arguments for subprocess.run() looks like the following list:

# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)

