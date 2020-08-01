
import zipfile
from tqdm import tqdm
import sys, os
print " fb.ibteesam chekhong ig.cang_5669"         
print " -----------------------------"
print  "--------------------------"
print  "-----------------------"
print  "-------------------"
print  "--------------"
print  "------------"
print "---------"
print  "-------"
print  "----"
print " Drag the file and don'n forgat this symbol. open End,End,End " 
print ' Example "root/desktop/assin.py"   '
print "########################################### "
print "###################################### "
print "############################### "
print "########################### "
print "###################### "
print "################## "
print "############### "
print "############ " 
print "######### "
print "##### "





























zip_file = input("Enter zipFile : ")
wordlist = input("Enter Passlist : ")





zip_file = zipfile.ZipFile(zip_file)

n_work = len(list(open(wordlist,"rb")))
with open(wordlist,"rb") as wordlist:
    for word in tqdm(wordlist,total=n_work,unit="files"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
                continue
        else:
                print("\n [+] password found",word.decode().strip())
                exit()

                
