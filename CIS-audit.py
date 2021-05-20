import os
import pwd
import subprocess  
import re
filename = ["/etc/shadow", "/etc/gshadow", "/etc/ssh/sshd_config", "/etc/passwd", "/etc/group"]
  
  
for filename in filename:
    filename_st = os.stat(filename)
    filename_uid = os.stat(filename).st_uid
    filename_owner = pwd.getpwuid(filename_st.st_uid).pw_name
    mask = oct(os.stat(filename).st_mode)[-3:]
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("File permission mask & owner for:", filename, mask, filename_owner)
    if mask =='000' or mask == '644' and filename_owner == 'root':
       print("*********Correct Permission/Owner*****************")
    else:
       print("<<<<<<<<<<< INCORRECT Permission/Owner >>>>>>>>>>>>")

print("================================================================================")

#print("Password complexity checking")
#password_file = open("/etc/security/pwquality.conf")
#readfile = password_file.read()
string =["minlen = 8", "dcredit = -1", "ucredit = -1", "ocredit = -1", "lcredit = -1"]
#string = re.match('^',input)
#for string in string:
#    if string in readfile:
#       print(string, 'Found in pwquality.conf file')
#    else:
#       print(string, 'Not found in pwquality.conf file')
#password_file.close()

for string in string:
    regex = subprocess.Popen(["grep", string, "/etc/security/pwquality.conf"], shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    print(subprocess_return)
    print(regex)
    if regex == string:
        print("Correct", regex)
    else:
        print("Incorrect")

import commands
status, output = commands.getstatusoutput(grep ,string  /etc/security/pwquality.conf)
print(status, output) 
