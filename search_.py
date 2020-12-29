import glob 
import os
import sys 

keywords = ["/bin/sh","popen","system","passw","token","secret", "dlopen","setreuid","upload","download","tar ","unzip"]
PATH=""
if (len(sys.argv[1]) > 2):
    PATH=sys.argv[1]+"/*"

else:
    PATH="./*"

for file_name in glob.glob(PATH):
    print("[+] %s " %(file_name))
    for keyword in keywords :
        os.system("strings %s | grep %s | awk {'print \"\t\"$0'}" % (file_name, keyword)) 

